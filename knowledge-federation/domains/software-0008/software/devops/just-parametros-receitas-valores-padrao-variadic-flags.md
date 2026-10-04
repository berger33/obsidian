---
id: software.devops.tranche12.001192
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://just.systems/man/en/", "https://raw.githubusercontent.com/casey/just/master/README.md", "https://github.com/casey/just"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# just: Parâmetros de Receitas, Valores Padrão, Argumentos Variádicos e Flags no justfile

## Em uma frase
Diferente do `make`, onde passar argumentos posicionais para um alvo exige gambiarra com variáveis de ambiente (`make deploy ENV=staging`), as receitas do `just` aceitam parâmetros posicionais tipados com valores padrão, argumentos variádicos (`+` para um ou mais, `*` para zero ou mais) e exportação direta para variáveis de ambiente (`$param`).

## Por que importa
Scripts de operação DevOps frequentemente precisam receber o ambiente alvo (`staging`, `prod`), a tag da imagem e flags extras para repassar ao `kubectl`, `helm` ou `pytest` de forma ergonômica e autodocumentada.

## Como funciona
No cabeçalho da receita, declara-se `deploy env="staging" +flags="--atomic":`; dentro do corpo, o valor é interpolado com `{{env}}` e `{{flags}}`, ou exportado automaticamente como variável de ambiente prefixando o parâmetro com `$` (`deploy $ENV="staging":`).

## Exemplo
```just
# Receita com parametro com default, exportacao de env e argumento variadico:
k8s-apply $KUBE_CTX="kind-dev" *kubectl_args="--dry-run=client":
  kubectl --context "$KUBE_CTX" apply -f k8s/ {{kubectl_args}}
```

## Limites e trade-offs
Esquecer de colocar espaços ao redor de `{{variavel}}` ou não colocar aspas quando o argumento pode conter espaços faz o shell dividir a string em múltiplos tokens inesperados.

## Como verificar
Prefira parâmetros exportados com `$` (`$PARAM`) quando o valor puder conter espaços ou caracteres especiais do shell, pois o `just` os passa via ambiente sem sofrer word splitting de interpolação textual.

## Conexões
- [[just-command-runner-justfile-diferencas-make-phony]] — Veja também: just: Command Runner Declarativo (justfile) e Eliminação de Idiossincrasias do Make.
- [[just-settings-set-shell-dotenv-load-positional-arguments-export]] — Veja também: just: Configurações de Comportamento no justfile (set shell, dotenv-load, export e positional-arguments).

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://just.systems/man/en/) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://raw.githubusercontent.com/casey/just/master/README.md) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
