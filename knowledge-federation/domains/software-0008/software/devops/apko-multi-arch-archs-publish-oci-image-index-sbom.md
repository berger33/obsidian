---
id: software.devops.tranche14.001367
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

# apko: Construção e Publicação Multi-Arquitetura (archs e apko publish) com Geração Automática de SBOM

## Em uma frase
A chave `archs` no `apko.yaml` (`386`, `amd64`, `arm64`, `arm/v6`, `arm/v7`, `ppc64le`, `riscv64`, `s390x`) combinada com o comando `apko publish` constrói e publica imagens multi-arquitetura e seus respectivos **SBOMs (Software Bill of Materials)** diretamente no registro OCI sem precisar de emulação QEMU.

## Por que importa
Construir uma imagem `arm64` em um runner `amd64` usando `docker buildx` com QEMU precisa emular instruções de CPU durante o `RUN`, tornando o build lento.

## Como funciona
Como o `apko` apenas baixa os pacotes `.apk` já compilados para cada arquitetura e monta os tarballs das camadas e o `OCI Image Index`, ele constrói imagens para 4 ou 6 arquiteturas em poucos segundos em qualquer máquina e gera um SBOM detalhando exatamente todos os pacotes instalados.

## Exemplo
```bash
apko publish examples/alpine-base.yaml ghcr.io/org/alpine-apko:v1.0.0 \
  --arch amd64,arm64
```

## Limites e trade-offs
Listar uma arquitetura em `archs` (como `riscv64` ou `s390x`) para a qual um dos pacotes customizados em `contents.packages` ainda não foi compilado faz a resolução de pacotes daquela arquitetura falhar.

## Como verificar
Garanta que todos os repositórios declarados em `contents.repositories` possuam os pacotes construídos para todas as arquiteturas listadas em `archs`.

## Conexões
- [[apko-paths-permissoes-diretorios-symlinks-hardlinks]] — Veja também: apko: Mutação Declarativa de Caminhos, Diretórios, Links e Permissões (paths).
- [[apko-layering-strategy-origin-budget-otimizacao-cache-camadas]] — Veja também: apko: Estratégia de Divisão em Camadas (layering.strategy e budget) para Eficiência de Pull.

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
