---
id: software.devops.tranche04.000394
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md", "https://docs.terragrunt.com/getting-started/quick-start/", "https://github.com/gruntwork-io/terragrunt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Funcionamento do diretório .terragrunt-cache e uso da função built-in get_terragrunt_dir()

## Em uma frase
Quando o Terragrunt executa comandos em uma unidade que referencia um módulo via `terraform { source = ... }`, ele cria um diretório especial **`.terragrunt-cache`** dentro do diretório da unidade. Conforme detalhado no Quick Start oficial, o `.terragrunt-cache` funciona como o diretório de rascunho (scratch directory) onde o Terragrunt baixa configurações remotas de OpenTofu/Terraform, armazena módulos e provedores baixados, grava arquivos gerados e executa os comandos sob um subdiretório `.terragrunt-cache/[HASH]/[HASH]/`. Por essa razão, caminhos relativos como `${path.module}` dentro do módulo apontam para dentro do cache; quando o usuário deseja referenciar o diretório onde o próprio `terragrunt.hcl` reside, deve passar a função built-in **`get_terragrunt_dir()`** via `inputs`.

## Por que importa
Se um módulo usa `${path.module}/hi.txt` achando que gravará no diretório da unidade, o arquivo será criado dentro de `.terragrunt-cache/[HASH]/[HASH]/hi.txt`. Compreender o papel do `.terragrunt-cache` e da função `get_terragrunt_dir()` evita confusão ao trabalhar com caminhos locais e artefatos gerados.

## Como funciona
Adicione sempre `.terragrunt-cache` ao arquivo `.gitignore` do repositório (da mesma forma que `.terraform`) e utilize `get_terragrunt_dir()` nos `inputs` do `terragrunt.hcl` sempre que o módulo precisar ler ou gravar arquivos relativos à pasta da unidade.

## Exemplo
Ao notar que o recurso `local_file` estava gravando `hi.txt` dentro de `.terragrunt-cache`, o engenheiro adiciona `variable "output_dir" {}` ao módulo compartilhado e define `output_dir = get_terragrunt_dir()` em `inputs` no `terragrunt.hcl`, passando a gerar o arquivo diretamente em `foo/hi.txt`.

## Limites e trade-offs
Nunca versione o diretório `.terragrunt-cache` no Git; como afirma a documentação oficial, você pode deletar essa pasta com segurança a qualquer momento e o Terragrunt a recriará automaticamente quando necessário.

## Como verificar
Verifique que `.terragrunt-cache` consta no `.gitignore` do projeto e confirme que o uso de `get_terragrunt_dir()` resolve para o caminho absoluto exato do diretório da unidade.

## Conexões
- [[terragrunt-units-shared-modules-and-inputs-blocks]] — Veja também: Unidades (units), módulos compartilhados e eliminação de main.tf redundantes com blocos terraform e inputs.
- [[terragrunt-stacks-and-concurrent-run-all-execution]] — Veja também: Gerenciamento de Stacks e execução concorrente com terragrunt run --all e --non-interactive.

## Fontes
- [Terragrunt GitHub — README.md (OpenTofu >= 1.6.0 & Terraform >= 0.12.0 Orchestration)](https://raw.githubusercontent.com/gruntwork-io/terragrunt/main/README.md) — README oficial do Terragrunt mantido pela Gruntwork sob licença MIT descrevendo orquestração flexível para escalar código IaC escrito em OpenTofu (>= 1.6.0) e Terraform (>= 0.12.0).; consultado em 2026-10-03.
- [Terragrunt Documentation — Quick Start (Auto-init, Units, Stacks, DAG, dependency & mock_outputs)](https://docs.terragrunt.com/getting-started/quick-start/) — Guia oficial de início rápido do Terragrunt detalhando terragrunt.hcl, Auto-init, --log-format bare (TG_LOG_FORMAT=bare), unidades (units), módulos compartilhados, blocos terraform e inputs, diretório .terragrunt-cache, get_terragrunt_dir(), execução em stack com terragrunt run --all, grafo acíclico direcionado (DAG), bloco dependency, mock_outputs e mock_outputs_allowed_terraform_commands, e Terragrunt Scale.; consultado em 2026-10-03.
- [Terragrunt — Official GitHub Repository](https://github.com/gruntwork-io/terragrunt) — Repositório oficial MIT do Terragrunt com código-fonte e fixtures de documentação em test/fixtures/docs/01-quick-start.; consultado em 2026-10-03.
