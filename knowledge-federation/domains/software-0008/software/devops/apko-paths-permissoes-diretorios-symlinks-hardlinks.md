---
id: software.devops.tranche14.001366
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

# apko: Mutação Declarativa de Caminhos, Diretórios, Links e Permissões (paths)

## Em uma frase
Como o `apko` não possui instruções `RUN mkdir`, `RUN chmod` ou `RUN ln -s`, ele disponibiliza a seção declarativa `paths` para criar diretórios vazios (`directory`), arquivos vazios (`empty-file`), links físicos (`hardlink`), links simbólicos (`symlink`) e ajustar permissões/propriedade (`permissions`, `uid`, `gid`).

## Por que importa
Um processo rodando como usuário não-root (`uid: 10000`) falha ao iniciar se precisar gravar arquivos temporários ou sockets PID em `/run/nginx` ou `/var/cache/app` e o diretório não existir ou pertencer ao `root`.

## Como funciona
Cada item na lista `paths` declara o `path`, o `type` (`directory`, `empty-file`, `hardlink`, `symlink` ou `permissions`), o `uid`/`gid` e as permissões em octal (`0o755`, `0o644`), aplicando as mutações deterministicamente na imagem.

## Exemplo
```yaml
paths:
  - path: /run/nginx
    type: directory
    uid: 10000
    gid: 10000
    permissions: 0o755
  - path: /etc/nginx/http.d/default.conf
    type: hardlink
    source: /usr/share/nginx/http-default_server.conf
    uid: 10000
    gid: 10000
    permissions: 0o644
```

## Limites e trade-offs
Definir apenas `uid: 10000` e omitir `gid` em um item de `paths` faz com que o `gid` assuma `0` (`root`) por padrão, conforme documentado na especificação do arquivo `apko`.

## Como verificar
Especifique sempre ambos `uid` e `gid` explicitamente em cada entrada de `paths` que requer propriedade de usuário não-root.

## Conexões
- [[apko-entrypoint-cmd-service-bundle-s6-supervision]] — Veja também: apko: Configuração de Entrypoint, Cmd, Stop-Signal e Supervisão Multi-Processo com s6 (service-bundle).
- [[apko-multi-arch-archs-publish-oci-image-index-sbom]] — Veja também: apko: Construção e Publicação Multi-Arquitetura (archs e apko publish) com Geração Automática de SBOM.

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
