---
id: software.devops.tranche14.001363
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

# apko: Separação entre Repositórios de Build e Runtime (runtime_repositories e runtime_keyring)

## Em uma frase
O `apko` distingue entre os repositórios usados no momento do build (`contents.repositories` e `contents.keyring`) e os repositórios/chaves que devem ficar gravados dentro da imagem final para uso futuro (`contents.runtime_repositories` e `contents.runtime_keyring`).

## Por que importa
Quando uma imagem base de desenvolvimento é construída no CI usando um cache local temporário, mas no container em execução o usuário precisa rodar `apk add` apontando para um mirror interno corporativo que re-assina o `APKINDEX`, as configurações de build e runtime são diferentes.

## Como funciona
A lista `runtime_repositories` é escrita em `/etc/apk/repositories` na imagem gerada sem ser consultada durante o build, enquanto `runtime_keyring` instala chaves públicas RSA PEM (`{name, content}`) em `/etc/apk/keys` após a resolução dos pacotes, servindo exclusivamente como âncora de confiança em runtime.

## Exemplo
```yaml
contents:
  repositories:
    - https://dl-cdn.alpinelinux.org/alpine/v3.22/main
  runtime_repositories:
    - https://apk-mirror.internal.corp/alpine/v3.22/main
  runtime_keyring:
    - name: corp-mirror.rsa.pub
      content: |
        -----BEGIN PUBLIC KEY-----
        ...
        -----END PUBLIC KEY-----
  packages:
    - alpine-base
```

## Limites e trade-offs
Definir um `name` em `runtime_keyring` que não coincide exatamente com o nome referenciado pela assinatura `.SIGN.RSA256.<name>` do `APKINDEX` do mirror faz o `apk add` falhar com erro de chave não confiável em runtime.

## Como verificar
Garanta que o campo `name` em `runtime_keyring` seja idêntico ao sufixo do arquivo `.SIGN.RSA256.<name>` gerado pelo repositório mirror.

## Conexões
- [[apko-contents-repositories-packages-keyring-local-repos]] — Veja também: apko: Configuração de contents (repositories, packages, keyring e Repositórios @local).
- [[apko-accounts-users-groups-run-as-nonroot-hardening]] — Veja também: apko: Configuração Declarativa de Contas Não-Privilegiadas (accounts, users, groups e run-as).

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
