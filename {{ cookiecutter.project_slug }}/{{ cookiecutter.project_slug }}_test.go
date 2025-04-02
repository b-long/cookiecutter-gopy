package {{ cookiecutter.project_slug }}

import "testing"

func TestHello(t *testing.T) {
	got := Hello("world")
	want := "Hello, world!\n"
	if got != want {
		t.Error("Unexpected value")
	}

}