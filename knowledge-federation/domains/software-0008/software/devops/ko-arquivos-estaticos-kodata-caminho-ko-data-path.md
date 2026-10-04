---
id: software.devops.tranche09.000867
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

# ko: empacotamento de arquivos estáticos sem Dockerfile usando o diretório kodata e KO_DATA_PATH

## Em uma frase
Para incluir arquivos estáticos (templates HTML, assets web, migrações SQL ou configurações) na imagem OCI sem usar um `Dockerfile` nem `COPY`, basta colocá-los em um subdiretório chamado **`kodata/`** dentro do pacote `main` e lê-los em runtime a partir do caminho na variável de ambiente **`KO_DATA_PATH`**.

## Por que importa
Embora binários Go modernos possam embutir pequenos arquivos no próprio executável usando `//go:embed`, muitas aplicações precisam distribuir diretórios de assets estáticos grandes, templates ou arquivos lidos diretamente do sistema de arquivos por bibliotecas que esperam um caminho em disco.

## Como funciona
Quando o `ko` constrói o pacote `./cmd/app`, ele verifica automaticamente se existe um diretório **`./cmd/app/kodata`** (ou um link simbólico `kodata` apontando para outra pasta do repositório). Se existir, o `ko` empacota todo o conteúdo de `kodata/` em uma camada separada da imagem OCI montada em `/var/run/ko` e define automaticamente na configuração da imagem a variável de ambiente **`KO_DATA_PATH=/var/run/ko`**. No código Go, basta ler `os.Getenv("KO_DATA_PATH")` (por exemplo, `filepath.Join(os.Getenv("KO_DATA_PATH"), "index.html")`) para acessar os arquivos em produção.

## Exemplo
```bash
# Criar o diretório kodata ao lado do main.go e verificar que o ko empacota os arquivos em /var/run/ko ($KO_DATA_PATH)
mkdir -p ./cmd/app/kodata
echo '{"env": "prod"}' > ./cmd/app/kodata/config.json
ko build ./cmd/app --local
```

## Limites e trade-offs
Como o `ko` coloca os arquivos de `kodata/` em uma camada OCI dedicada separada da camada do binário `/ko-app/app`, se você alterar apenas o código `.go` sem tocar em `kodata/`, a camada de dados estáticos é 100% reutilizada no registry; lembre-se apenas de definir `KO_DATA_PATH=./cmd/app/kodata` ao rodar `go run ./cmd/app` fora de containers na máquina local caso seu código espere essa variável.

## Como verificar
Inspecione a configuração da imagem gerada com `docker inspect <imagem> --format '{{.Config.Env}}'` e confirme a presença de `KO_DATA_PATH=/var/run/ko`.

## Conexões
- [[ko-desenvolvimento-local-ko-local-kind-local-minikube]] — Veja também: ko: publicação direta para o daemon Docker local (ko.local / --local) e clusters kind (kind.local).
- [[ko-nomenclatura-imagens-base-import-paths-preserve-import-paths]] — Veja também: ko: estratégias de nomenclatura de imagens no registry (--base-import-paths, --preserve-import-paths e --bare).
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[ko-configuracao-ko-yaml-imagens-base-flags-ldflags]] — Referência cruzada direta com ko-configuracao-ko-yaml-imagens-base-flags-ldflags.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
