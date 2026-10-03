---
id: software.devops.tranche12.001196
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

# just: Grafo de Dependências de Receitas (Pré-Dependências, Pós-Dependências e Passagem de Argumentos)

## Em uma frase
As receitas do `just` suportam pré-dependências (executadas antes da receita principal), pós-dependências prefixadas com `&&` (executadas logo após o término bem-sucedido da receita) e passagem de argumentos parametrizados para dependências entre parênteses (`build: (setup "prod")`).

## Por que importa
Em fluxos de release e deploy, muitas vezes é necessário garantir que validações rodem antes do build (`lint`, `test`) e que tarefas de limpeza ou notificação rodem após o deploy sem duplicar chamadas dentro do corpo de cada script.

## Como funciona
Na sintaxe `deploy env: (validate env) && (notify env)`, o `just` constrói o grafo acíclico de execução, garante que `validate` rode primeiro com o argumento `env`, executa o corpo de `deploy` e, se retornar código zero, aciona `notify` em seguida.

## Exemplo
```just
validate env:
  @echo "Validando configuracao de {{env}}..."

notify env:
  @echo "Deploy concluido em {{env}}!"

deploy env="staging": (validate env) && (notify env)
  @echo "Aplicando manifestos em {{env}}..."
```

## Limites e trade-offs
Assumir que uma pós-dependência (`&& cleanup`) será executada mesmo quando a receita principal falhar deixa recursos temporários órfãos, pois pós-dependências no `just` só rodam se a receita anterior tiver sucesso.

## Como verificar
Para limpezas que precisam rodar mesmo em caso de erro (`finally`), utilize `trap ... EXIT` dentro de uma receita shebang `#!/usr/bin/env bash`.

## Conexões
- [[just-expressoes-funcoes-embutidas-arch-os-env-var-sha256]] — Veja também: just: Linguagem de Expressões, Condicionais e Funções Embutidas (os(), arch(), env_var(), sha256()).
- [[just-modulos-imports-organizacao-monorepos-devops]] — Veja também: just: Organização de Monorepos e Plataformas com import e Módulos (mod).

## Fontes
- [just GitHub — README.md (justfile Syntax, Improvements over Make, Settings, Shebang Recipes, Modules & Cross-Platform Packages)](https://just.systems/man/en/) — README oficial do casey/just detalhando diferenças em relação ao make (sem .PHONY), parâmetros de receitas, carregamento de .env, receitas shebang, módulos/imports e instalação multiplataforma; consultado em 2026-10-03.
- [Just Programmer's Manual — Official Book (just.systems/man/en/)](https://raw.githubusercontent.com/casey/just/master/README.md) — Manual oficial completo do just documentando expressões, funções embutidas, atributos de receita ([confirm], [private], [no-cd]), dependências pré/pós e shell completions; consultado em 2026-10-03.
- [just — Official GitHub Repository](https://github.com/casey/just) — Repositório oficial do casey/just; consultado em 2026-10-03.
