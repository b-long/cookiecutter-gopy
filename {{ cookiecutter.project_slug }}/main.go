package {{ cookiecutter.project_slug }}

import "fmt"

func Hello(name string) {
    fmt.Printf("Hello, %s!\\n", name)
}