import json
import pytest
from apps.profiles.renderers import ProfileJSONRenderer  # adjust the import path as needed

@pytest.fixture
def renderer():
    return ProfileJSONRenderer()

def test_profile_renderer_normal_data(renderer):
    """
    When no errors are present in the data, the renderer should wrap the data
    inside a "profile" key.
    """
    data = {
        "username": "testuser",
        "email": "test@example.com"
    }
    
    # Render the data using our custom renderer.
    rendered = renderer.render(data)
    
    # json.dumps returns a string so convert the rendered output to a dict.
    rendered_data = json.loads(rendered)
    
    expected = {"profile": data}
    
    assert rendered_data == expected, "The renderer should wrap the data under 'profile' key."

def test_profile_renderer_error_data(renderer):
    """
    When errors are present, the renderer should return the data as-is
    in the default JSON format (i.e. not wrapped).
    """
    data = {
        "errors": {"username": ["This field is required."]}
    }
    
    # Render the data with errors
    rendered = renderer.render(data)
    
    # The default JSONRenderer.render produces a bytestring for errors.
    # Convert rendered output from bytes to a string (if necessary)
    if isinstance(rendered, bytes):
        rendered = rendered.decode(renderer.charset)
    
    rendered_data = json.loads(rendered)
    
    # Because the errors key is present, the renderer delegates the formatting to the base renderer.
    # Thus the output should be the same as the input data.
    assert rendered_data == data, "The renderer should not wrap error responses."
