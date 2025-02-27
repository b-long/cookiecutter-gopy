package {{ cookiecutter.project_slug }}

func TestHello(t *testing.T) {
	got := {{ cookiecutter.project_slug }}.Hello()
	want := "Hello, world"
	if got != want {
		t.Error("Unexpected value")
	}

}
