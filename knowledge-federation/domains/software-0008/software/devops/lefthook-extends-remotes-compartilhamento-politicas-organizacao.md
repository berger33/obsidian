---
id: software.devops.tranche13.001278
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://lefthook.dev/usage/", "https://lefthook.dev/configuration/", "https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lefthook: Compartilhamento de Políticas entre Repositórios com extends e remotes

## Em uma frase
Por meio das diretivas `extends` e `remotes` no `lefthook.yml`, uma equipe de plataforma ou segurança pode manter um repositório central de hooks corporativos (como varredura de segredos `gitleaks`/`trufflehog`, lint de commits e verificação de licenças) e herdá-lo automaticamente em dezenas de repositórios de microsserviços.

## Por que importa
Copiar e atualizar manualmente a mesma configuração de scanner de segredos em 150 repositórios Git faz com que novas regras de segurança demorem meses para chegar a todos os projetos.

## Como funciona
Com `remotes` apontando para o `git_url` do repositório de políticas da organização (fixado por `ref` de tag ou branch) e o caminho do `configs`, o Lefthook baixa e mescla as regras remotas com o `lefthook.yml` local. O comando `lefthook dump` exibe exatamente a configuração final resultante da fusão de `remotes`, `extends` e `lefthook-local.yml`.

## Exemplo
```yaml
remotes:
  - git_url: https://github.com/org/platform-git-hooks
    ref: v1.2.0
    configs:
      - security-pre-commit.yml
```

## Limites e trade-offs
Apontar `remotes.git_url` para a branch `main` sem fixar uma tag `ref` auditada permite que uma alteração incorreta no repositório central quebre o `git commit` de todos os desenvolvedores da empresa simultaneamente.

## Como verificar
Fixe sempre `ref` em uma tag semântica revisada (`v1.2.0`) na seção `remotes` e valide a configuração resultante com `lefthook dump` e `lefthook validate`.

## Conexões
- [[lefthook-bypass-emergencia-lefthook-0-output-control]] — Veja também: Lefthook: Controle de Verbose (output) e Bypass Consciente em Emergências (LEFTHOOK=0).
- [[lefthook-seguranca-shift-left-gitleaks-trivy-kubeconform-tflint]] — Veja também: Lefthook: Prevenção Shift-Left de Vazamento de Segredos e Erros IaC no pre-commit DevOps.

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://lefthook.dev/usage/) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://lefthook.dev/configuration/) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
