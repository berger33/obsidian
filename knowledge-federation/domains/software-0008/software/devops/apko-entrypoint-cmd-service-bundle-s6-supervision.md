---
id: software.devops.tranche14.001365
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md", "https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md", "https://github.com/chainguard-dev/apko"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# apko: Configuração de Entrypoint, Cmd, Stop-Signal e Supervisão Multi-Processo com s6 (service-bundle)

## Em uma frase
A seção `entrypoint` do `apko` suporta tanto a definição direta do comando principal (`entrypoint.command`, `cmd` e `stop-signal`) quanto o modo `type: service-bundle`, que utiliza a suíte de supervisão **s6** para gerenciar múltiplos processos dentro do mesmo container sem problemas de processos zumbis (reaping) ou propagação de sinais.

## Por que importa
Quando um container precisa rodar dois processos acoplados e o processo PID 1 não trata sinais UNIX nem recolhe processos filhos órfãos, o desligamento do Pod fica preso até o `terminationGracePeriodSeconds` expirar.

## Como funciona
Definindo `entrypoint.type: service-bundle` e mapeando os comandos em `entrypoint.services`, o `apko` configura o supervisor **s6** como PID 1 para iniciar e monitorar os serviços declarados.

## Exemplo
```yaml
entrypoint:
  type: service-bundle
  services:
    nginx: /usr/sbin/nginx -c /etc/nginx/nginx.conf -g "daemon off;"

stop-signal: SIGQUIT
work-dir: /usr/share/nginx
```

## Limites e trade-offs
Configurar um `stop-signal` customizado (como `SIGQUIT`) junto com `entrypoint.type: service-bundle` exige atenção, pois o supervisor `s6` intercepta e pode reinterpretar o sinal de desligamento enviado pelo runtime.

## Como verificar
Para containers de processo único (padrão recomendado em Kubernetes), use `entrypoint.command` direto; reserve `type: service-bundle` apenas quando a supervisão `s6` for estritamente necessária.

## Conexões
- [[apko-accounts-users-groups-run-as-nonroot-hardening]] — Veja também: apko: Configuração Declarativa de Contas Não-Privilegiadas (accounts, users, groups e run-as).
- [[apko-paths-permissoes-diretorios-symlinks-hardlinks]] — Veja também: apko: Mutação Declarativa de Caminhos, Diretórios, Links e Permissões (paths).

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
