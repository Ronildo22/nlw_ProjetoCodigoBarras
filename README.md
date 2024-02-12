# Configurando o Pylint

```bat
    pylint --generate-rcfile > .pylintrc
```

## No arquivo que for gerado fazer os itens abaixo:


```python
    disable=
        C1477, # descrição do pylint
```

## Apos desabilitar a verificação do pylint, abrir e fechar o arquivo py onde vc deseja remover a verificação


## Para executar o pylint, sempre que realizar um commit local:

- Instale a lib `pip install pre-commit`
- Crie um arquivo chamado `.pre-commit-config.yaml`
- Insira o script abaixo no arquivo .yaml:

```yaml
repos:
  - repo: local
    hooks:
      - id: pylint
        name: pylint
        entry: pylint
        language: system
        types: [python]
        args:
          [
            "-rn", # Only display messages
            "-sn", # Don't display the source
            "--rcfile=.pylintrc", # Link to your config file
            "--load-plugins=pylint.extensions.docparams", # Load an extension
          ]
```

- Execute o comando `pre-commit install`

Pronto agora você pode realizar um commit de teste para verificar a execução do pylint

### Exemplo de execução do pylint abaixo:

<img src="/docs/img/exemple_execute_pylint.png" alt="Image with example execute pylint" style="align: center;">


## Para executar os testes unitarios usando o pytest, utilize:

```bat
  pytest
```

### Para uma execução mais detalhada utilize:

```bat
  pytest -s -v
```
