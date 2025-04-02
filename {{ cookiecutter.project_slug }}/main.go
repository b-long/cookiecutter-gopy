package {{ cookiecutter.project_slug }}

import "fmt"

func Hello(name string) string {
	return fmt.Sprintf("Hello, %s!\n", name)
}
