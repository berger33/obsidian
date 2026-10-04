---
id: software.devops.tranche13.001279
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
fontes: ["https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md", "https://lefthook.dev/configuration/", "https://lefthook.dev/usage/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Lefthook: Prevenção Shift-Left de Vazamento de Segredos e Erros IaC no pre-commit DevOps

## Em uma frase
Em repositórios de infraestrutura como código (Terraform, Kubernetes, Helm, Ansible), configurar o Lefthook para executar scanners rápidos sobre `{staged_files}` no `pre-commit` bloqueia o vazamento de credenciais (AWS keys, tokens GitHub, chaves privadas PEM) antes mesmo que elas entrem no histórico local do Git.

## Por que importa
Uma vez que um segredo é commitado e enviado por `git push` para o repositório remoto, mesmo que seja revertido no commit seguinte, a credencial já foi exposta aos logs de auditoria e requer revogação e rotação imediatas.

## Como funciona
Combinando `parallel: true` no `pre-commit`, o Lefthook executa simultaneamente `gitleaks protect --staged --redact`, `terraform fmt -check`, `tflint` e `kubeconform` apenas nas pastas e extensões modificadas, concluindo a verificação em menos de um segundo.

## Exemplo
```yaml
pre-commit:
  parallel: true
  jobs:
    - name: gitleaks-staged
      run: gitleaks protect --staged --no-banner --redact
    - name: helm-lint
      glob: "charts/**"
      run: helm lint charts/*
```

## Limites e trade-offs
Rodar `gitleaks detect` sobre todo o histórico de commits do repositório dentro do hook `pre-commit` (em vez de `gitleaks protect --staged`) torna cada commit lento à medida que o histórico Git cresce.

## Como verificar
No hook `pre-commit`, escaneie apenas o índice atual (`--staged` ou `{staged_files}`), deixando varreduras de histórico completo para o CI.

## Conexões
- [[lefthook-extends-remotes-compartilhamento-politicas-organizacao]] — Veja também: Lefthook: Compartilhamento de Políticas entre Repositórios com extends e remotes.
- [[lefthook-integracao-ci-cd-paridade-local-github-actions]] — Veja também: Lefthook: Execução de lefthook run no Pipeline de CI/CD para Paridade Total com Hooks Locais.

## Fontes
- [Lefthook GitHub — README.md (Fast Polyglot Git Hooks Manager in Go, Parallel Execution, File Placeholders, root & Scripts)](https://raw.githubusercontent.com/evilmartians/lefthook/master/README.md) — README oficial do evilmartians/lefthook detalhando paralelismo, placeholders ({staged_files}, {push_files}, {all_files}), filtros glob/exclude, suporte a monorepos com root e stage_fixed; consultado em 2026-10-03.
- [Lefthook Official Documentation — Configuration & Usage (lefthook.yml, lefthook-local.yml, remotes, validate, dump & LEFTHOOK=0)](https://lefthook.dev/configuration/) — Documentação oficial de configuração e uso da CLI do Lefthook cobrindo lefthook install, run, validate, dump, overrides locais e herança de configurações remotas; consultado em 2026-10-03.
- [Lefthook — Official CLI Usage Guide](https://lefthook.dev/usage/) — Guia oficial de comandos do Lefthook; consultado em 2026-10-03.
