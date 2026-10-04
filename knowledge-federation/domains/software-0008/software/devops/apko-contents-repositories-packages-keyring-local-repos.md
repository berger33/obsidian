---
id: software.devops.tranche14.001362
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

# apko: Configuração de contents (repositories, packages, keyring e Repositórios @local)

## Em uma frase
A seção de topo `contents` no arquivo YAML do `apko` define integralmente os arquivos que existirão na imagem por meio das chaves `repositories`, `packages`, `keyring`, `runtime_repositories` e `runtime_keyring`.

## Por que importa
Combinar pacotes oficiais de uma distribuição (como Wolfi ou Alpine) com pacotes `.apk` recém-construídos localmente no mesmo pipeline de CI requer referenciar diretórios locais verificados por assinatura.

## Como funciona
Em `contents.repositories`, podem ser listadas URLs HTTPS ou caminhos locais precedidos por uma tag de alias como `@local /github/workspace/packages`; em seguida, referencia-se o pacote correspondente em `contents.packages` com `meu-pacote@local` e incluem-se as chaves públicas de verificação em `contents.keyring`.

## Exemplo
```yaml
contents:
  repositories:
    - https://packages.wolfi.dev/os
    - "@local /work/packages"
  keyring:
    - https://packages.wolfi.dev/os/wolfi-signing.rsa.pub
    - /work/melange.rsa.pub
  packages:
    - wolfi-baselayout
    - custom-app@local
```

## Limites e trade-offs
Declarar um repositório local com o prefixo `@local /caminho` em `repositories` mas esquecer de adicionar o sufixo `@local` ao nome do pacote em `packages` faz o `apko` procurar o pacote apenas nos repositórios remotos padrão.

## Como verificar
Use sempre o sufixo `@local` no nome do pacote quando o repositório local for declarado com tag `@local`.

## Conexões
- [[apko-arquitetura-construtor-imagens-oci-apk-reprodutivel]] — Veja também: apko: Construtor Declarativo de Imagens OCI Baseadas em APK Totalmente Reprodutíveis.
- [[apko-runtime-repositories-runtime-keyring-espelhos-internos]] — Veja também: apko: Separação entre Repositórios de Build e Runtime (runtime_repositories e runtime_keyring).

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
