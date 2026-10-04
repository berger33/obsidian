---
id: software.devops.tranche14.001361
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
fontes: ["https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md", "https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md", "https://github.com/chainguard-dev/apko"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# apko: Construtor Declarativo de Imagens OCI Baseadas em APK Totalmente Reprodutíveis

## Em uma frase
O **apko** (`chainguard-dev/apko`, criado pela Chainguard e inspirado pelos projetos `ko` e `distroless`) é uma ferramenta declarativa que constrói e publica imagens de container **OCI** diretamente a partir de pacotes **APK** (Wolfi ou Alpine Linux) em milissegundos, sem usar `Dockerfile` nem instruções `RUN`.

## Por que importa
Em um `Dockerfile` tradicional, cada execução de `RUN apk update && apk add ...` grava timestamps variáveis, caches e metadados não-determinísticos nas camadas, produzindo um digest SHA-256 diferente a cada build mesmo quando os pacotes não mudaram.

## Como funciona
Por design, o `apko` não suporta execução de comandos arbitrários durante o build: ele resolve o grafo de pacotes APK declarados em um arquivo YAML (`apko.yaml`), monta o sistema de arquivos de forma determinística (**bitwise reproducible** — rodar duas vezes gera exatamente o mesmo binário/digest) e emite automaticamente o SBOM completo da imagem.

## Exemplo
```bash
apko version
apko build examples/alpine-base.yaml apko-alpine:test apko-alpine.tar
docker load < apko-alpine.tar
```

## Limites e trade-offs
Tentar colocar comandos de compilação ou scripts de instalação (`curl | sh`) dentro do `apko.yaml` não é suportado porque o `apko` é estritamente um montador declarativo de pacotes APK.

## Como verificar
Empacote previamente aplicações próprias como pacotes `.apk` usando o **melange** e utilize o **apko** para compor a imagem OCI final.

## Conexões
- [[apko-contents-repositories-packages-keyring-local-repos]] — Veja também: apko: Configuração de contents (repositories, packages, keyring e Repositórios @local).

## Fontes
- [apko GitHub — README.md (APK-Based Reproducible OCI Image Builder, apko build, apko publish, SBOM Generation & Declarative Design)](https://raw.githubusercontent.com/chainguard-dev/apko/main/README.md) — README oficial do chainguard-dev/apko detalhando reprodutibilidade bitwise sem instruções RUN, geração automática de SBOM, integração com melange e supervisão s6; consultado em 2026-10-03.
- [apko Official Documentation — docs/apko_file.md (contents, repositories, runtime_keyring, entrypoint, accounts, paths, archs & layering)](https://raw.githubusercontent.com/chainguard-dev/apko/main/docs/apko_file.md) — Referência completa do formato YAML do apko cobrindo repositórios @local, runtime_repositories/runtime_keyring, accounts non-root, mutações de paths e layering.strategy; consultado em 2026-10-03.
- [Chainguard apko — Official GitHub Repository](https://github.com/chainguard-dev/apko) — Repositório oficial Apache-2.0 do apko; consultado em 2026-10-03.
