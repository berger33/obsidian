---
id: software.devops.tranche09.000866
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

# ko: publicação direta para o daemon Docker local (ko.local / --local) e clusters kind (kind.local)

## Em uma frase
Para desenvolvimento local sem registry remoto, o `ko` reconhece os destinos especiais `KO_DOCKER_REPO=ko.local` (ou flag `--local` / `-L`, que carrega a imagem diretamente no daemon Docker local) e `KO_DOCKER_REPO=kind.local` (que injeta a imagem diretamente dentro de um cluster `kind` ativo).

## Por que importa
Durante o desenvolvimento local de um operador Kubernetes ou microsserviço em Go rodando em um cluster **`kind`**, fazer push de cada build de teste para um registry na nuvem e esperar o `kubelet` baixar pela internet desperdiça tempo e banda; da mesma forma, rodar `docker build` + `kind load docker-image` exige passos extras. O `ko` integra nativamente tanto o Docker local quanto o `kind`.

## Como funciona
Em vez de apontar `KO_DOCKER_REPO` para um registry remoto: (1) ao definir **`KO_DOCKER_REPO=ko.local`** (ou passar a flag **`ko build --local`** / **`-L`**), o `ko` exporta a imagem construída diretamente para o daemon Docker local da estação de trabalho sem fazer push para a internet; e (2) ao definir **`KO_DOCKER_REPO=kind.local`** (e opcionalmente `KIND_CLUSTER_NAME=<nome>` caso o cluster não se chame `kind`), executar `ko build ./cmd/app` ou **`KO_DOCKER_REPO=kind.local ko apply -f config/`** compila o binário Go no host, monta a imagem OCI em memória, carrega-a diretamente dentro dos nós do cluster `kind` e aplica o manifesto Kubernetes resolvido com o digest `@sha256:...` em segundos.

## Exemplo
```bash
# Compilar um controlador Go, injetar a imagem diretamente no cluster kind local e aplicar o manifesto em um único comando
KO_DOCKER_REPO=kind.local ko apply -f config/
```

## Limites e trade-offs
Ao usar `KO_DOCKER_REPO=kind.local`, o `ko` constrói a imagem para a arquitetura do nó do cluster `kind` local; se o seu cluster `kind` tiver um nome customizado diferente do padrão `kind` (criado com `kind create cluster --name meu-cluster`), você **deve** exportar `export KIND_CLUSTER_NAME=meu-cluster`, caso contrário o `ko` tentará carregar a imagem no cluster padrão `kind` e falhará se ele não existir.

## Como verificar
Com um cluster `kind` ativo, execute `KO_DOCKER_REPO=kind.local ko build ./cmd/app` e confirme com `docker exec -it kind-control-plane crictl images | grep kind.local` que a imagem foi injetada diretamente no nó.

## Conexões
- [[ko-configuracao-ko-yaml-imagens-base-flags-ldflags]] — Veja também: ko: customização de imagem base (defaultBaseImage), flags de compilação e ldflags com .ko.yaml.
- [[ko-arquivos-estaticos-kodata-caminho-ko-data-path]] — Veja também: ko: empacotamento de arquivos estáticos sem Dockerfile usando o diretório kodata e KO_DATA_PATH.
- [[ko-construtor-imagens-containers-go-sem-docker]] — Referência cruzada direta com ko-construtor-imagens-containers-go-sem-docker.
- [[ko-integracao-kubernetes-ko-resolve-apply-delete-uri]] — Referência cruzada direta com ko-integracao-kubernetes-ko-resolve-apply-delete-uri.
- [[kind-carregamento-imagens-locais-load-docker-image-archive]] — Referência cruzada direta com kind-carregamento-imagens-locais-load-docker-image-archive.

## Fontes
- [ko GitHub — README.md (Fast Go Container Builder, Multi-Platform, Automatic SBOMs & Bazel Heritage)](https://raw.githubusercontent.com/ko-build/ko/main/README.md) — README oficial do ko-build/ko (CNCF Sandbox) cobrindo compilação local Go sem Docker, suporte multiplataforma, geração de SBOM por padrão e integração com YAML do Kubernetes; consultado em 2026-10-03.
- [ko Official Documentation — Get Started (Authentication, KO_DOCKER_REPO, Naming Strategies & Local Publishing)](https://ko.build/get-started/) — Guia oficial Get Started do ko detalhando autenticação nativa (GCR/GAR, ECR, ACR, GHCR e ko login), KO_DOCKER_REPO, entrypoint /ko-app/<app>, estratégias de nomes (-B, -P, --bare) e destinos locais ko.local e kind.local; consultado em 2026-10-03.
- [ko Official Documentation — Kubernetes Integration (ko:// Importpaths, ko resolve, ko apply & ko delete)](https://ko.build/features/k8s/) — Documentação oficial de integração do ko com manifestos Kubernetes usando referências ko://, ko resolve, ko apply e ko delete; consultado em 2026-10-03.
