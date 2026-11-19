# Prova prática de Engenharia de Software II — Modelo 2

**Aluno:** Gustavo Origuela Fernandes Tricarico  
**Matrícula:** 1142644298  
**Modelo:** 2 — Loja MercadoBairro  
**D:** 8  
**LIMITE = MAXIMO:** 20 + 8 = **28%**

## Situação-problema

O MercadoBairro precisa validar o percentual de desconto de cupons cadastrados pelo gerente antes de salvá-los. O sistema só aceita números inteiros entre 1 e 28, inclusive.

## Requisitos

| ID | Regra |
| --- | --- |
| RF01 | Percentual inteiro entre 1 e 28, inclusive, é aceito. |
| RF02 | Percentual acima de 28 é rejeitado. |
| RF03 | Percentual zero ou negativo é rejeitado. |
| RF04 | Percentual não inteiro é rejeitado, mesmo dentro da faixa. |

## Arquivos

- `cupom.py`: função `desconto_valido(percentual)` e constante `MAXIMO = 28`.
- `test_cupom.py`: testes automatizados usando pytest.
- `.github/workflows/testes.yml`: testes na main e nos pull requests.
- `diagramas/casos_de_uso.drawio`: diagrama de casos de uso editável no draw.io.
- `diagramas/atividades.drawio`: diagrama de atividades editável no draw.io.

## Como testar

```bash
python -m pip install pytest
python -m pytest -v
```

## Fluxo de trabalho

A primeira execução dos testes deve revelar o defeito de limite superior do código inicial. O defeito é corrigido na `main` com a menor alteração possível. Depois, o requisito RF04 é implementado em branch separada, com issue e pull request para revisão de `@rafsp`. O PR não deve ser mesclado pelo aluno.
