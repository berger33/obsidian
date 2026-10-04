---
id: software.devops.tranche14.001364
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

# apko: Configuração Declarativa de Contas Não-Privilegiadas (accounts, users, groups e run-as)

## Em uma frase
A seção `accounts` do `apko.yaml` cria usuários (`users`), grupos (`groups`) e define o usuário padrão de execução do container (`run-as`) de forma puramente declarativa, sem precisar executar `adduser` ou `useradd` em um shell.

## Por que importa
Em imagens mínimas distroless onde não há `/bin/sh` nem utilitários shadow instalados na imagem final, não é possível rodar um comando `RUN useradd` dentro do container para criar o usuário não-root.

## Como funciona
O `apko` manipula diretamente os arquivos `/etc/passwd` e `/etc/group` da imagem durante a montagem da camada, registrando os `uid` e `gid` determinísticos (como `uid: 10000` ou `65532`) e gravando `run-as` na configuração da imagem OCI.

## Exemplo
```yaml
accounts:
  groups:
    - groupname: appgroup
      gid: 10000
  users:
    - username: appuser
      uid: 10000
      gid: 10000
      shell: /sbin/nologin
  run-as: appuser
```

## Limites e trade-offs
Omitir a seção `accounts` e `run-as` faz com que o processo principal da imagem OCI seja configurado para rodar como `root` (`UID 0`), violando políticas Kubernetes Pod Security Standards (`restricted`).

## Como verificar
Defina sempre um usuário não-root explícito em `accounts.users` e configure `accounts.run-as` em todas as imagens de produção construídas com `apko`.

## Conexões
- [[apko-runtime-repositories-runtime-keyring-espelhos-internos]] — Veja também: apko: Separação entre Repositórios de Build e Runtime (runtime_repositories e runtime_keyring).
- [[apko-entrypoint-cmd-service-bundle-s6-supervision]] — Veja também: apko: Configuração de Entrypoint, Cmd, Stop-Signal e Supervisão Multi-Processo com s6 (service-bundle).

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
