---
id: software.devops.tranche09.000865
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/ko-build/ko/main/README.md", "https://ko.build/get-started/", "https://ko.build/features/k8s/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# ko: customização de imagem base (defaultBaseImage), flags de compilação e ldflags com .ko.yaml

## Em uma frase
O arquivo de configuração `.ko.yaml` permite customizar a imagem base global (`defaultBaseImage`), definir imagens base por pacote (`baseImageOverrides`) e configurar opções do `go build` (`builds`, `flags`, `ldflags` e `env`) por binário.

## Por que importa
Embora o comportamento zero-configuração do `ko` (usando `cgr.dev/chainguard/static:latest`) atenda à maioria dos serviços, projetos reais em produção quase sempre precisam injetar a versão do Git no binário via `-ldflags "-s -w -X main.version={{.Env.VERSION}}"` ou usar uma imagem base específica (como Alpine/Wolfi com certificados ou tzdata customizados) para determinados binários.

## Como funciona
Quando o `ko` é executado em um diretório que contém um arquivo **`.ko.yaml`** (ou via variável `KO_CONFIG_PATH`), ele carrega: (1) **`defaultBaseImage`**: substitui a imagem base padrão para todos os pacotes; (2) **`baseImageOverrides`**: mapa que associa pacotes Go específicos a imagens base diferentes; (3) **`defaultPlatforms`**: lista padrão de arquiteturas (ex.: `["linux/amd64", "linux/arm64"]`) para não precisar passar `--platform` na CLI; e (4) **`builds`**: lista de configurações de compilação por `id`/`main` onde é possível declarar `env`, `flags` (ex.: `-trimpath`) e `ldflags` com suporte a templates `{{.Env.VAR}}` e `{{.Date}}`.

## Exemplo
```yaml
# Exemplo de arquivo .ko.yaml definindo imagem base padrão, plataformas multi-arch e ldflags de versão
defaultBaseImage: cgr.dev/chainguard/static:nonroot
defaultPlatforms:
  - linux/amd64
  - linux/arm64
builds:
  - id: api-server
    main: ./cmd/api
    flags:
      - -trimpath
    ldflags:
      - -s -w
      - -X main.version={{.Env.RELEASE_VERSION}}
```

## Limites e trade-offs
Ao trocar `defaultBaseImage` no `.ko.yaml` por uma imagem base em um registry privado ou corporativo, certifique-se de que a imagem base escolhida seja um manifesto multi-arquitetura caso você tenha configurado `defaultPlatforms: [linux/amd64, linux/arm64]`, pois o `ko` precisa encontrar na imagem base os descritores correspondentes a cada arquitetura alvo.

## Como verificar
Defina `-X main.version=v1.2.3` em `ldflags` no `.ko.yaml`, construa a imagem com `ko build ./cmd/api --local` e execute `docker run --rm <imagem> --version` para confirmar a injeção da versão no binário `/ko-app/api`.

## Conexões
- [[ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade]] — Veja também: ko: builds multiplataforma (--platform=all), geração de SBOM por padrão e reprodutibilidade.
- [[ko-desenvolvimento-local-ko-local-kind-local-minikube]] — Veja também: ko: publicação direta para o daemon Docker local (ko.local / --local) e clusters kind (kind.local).
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[ko-arquivos-estaticos-kodata-caminho-ko-data-path]] — Referência cruzada direta com ko-arquivos-estaticos-kodata-caminho-ko-data-path.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
