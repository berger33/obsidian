---
id: software.devops.tranche09.000883
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
fontes: ["https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md", "https://telepresence.io/docs/concepts/architecture", "https://github.com/telepresenceio/telepresence"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Telepresence: interceptações seletivas por cabeçalho HTTP (--http-header) e caminho (--http-path-*) em clusters compartilhados

## Em uma frase
O recurso de **Traffic Filtering** do Telepresence permite interceptar apenas as requisições que pertencem ao desenvolvedor (selecionadas por cabeçalho HTTP ou caminho de URL), deixando todas as demais requisições fluírem normalmente para o container original no cluster.

## Por que importa
Manter um cluster Kubernetes completo separado na nuvem para cada desenvolvedor da empresa é caro; porém, compartilhar um único cluster de desenvolvimento/staging só funciona se 20 desenvolvedores puderem depurar o mesmo microsserviço simultaneamente sem que um roube as requisições de teste do outro. O README oficial do Telepresence destaca o `Traffic filtering` como peça central para equipes compartilharem um único cluster sem colisões.

## Como funciona
Ao iniciar um `telepresence intercept` passando flags de filtragem HTTP — como **`--http-header x-dev-user=alice`** ou **`--http-path-prefix /api/v2/experimental`** (ou `--http-path-equal` / `--http-path-regex`) — o `Traffic Agent` atua como um proxy inteligente de camada 7 na frente do container do pod: para cada requisição HTTP recebida, ele inspeciona os cabeçalhos e o path; se a requisição contiver `x-dev-user: alice`, o `Traffic Agent` a desvia pelo túnel para a porta local na estação de trabalho da Alice; caso contrário, repassa a requisição imediatamente para o container original rodando dentro do pod no cluster.

## Exemplo
```bash
# Interceptar apenas requisições que contenham o cabeçalho HTTP x-dev-session=dev-alice sem afetar outros usuários do cluster
telepresence intercept orders-api --port 3000:8080 --http-header x-dev-session=dev-alice
```

## Limites e trade-offs
Para que a filtragem seletiva por cabeçalhos HTTP (`--http-header`) funcione em chamadas em cadeia (onde o frontend chama o `api-gateway`, que por sua vez chama o `orders-api` interceptado lá no fundo do cluster), os serviços intermediários precisam propagar o cabeçalho de contexto (como `baggage` do W3C Trace Context / OpenTelemetry ou cabeçalhos `x-dev-*`) nas chamadas downstream.

## Como verificar
Com o intercept filtrado ativo, envie um `curl` sem o cabeçalho `x-dev-session` (confirmando que o pod do cluster responde) e um segundo `curl -H "x-dev-session: dev-alice"` (confirmando que o processo local na sua IDE recebe a chamada).

## Conexões
- [[telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest]] — Veja também: Telepresence: os 4 modos de anexação a workloads (replace, intercept, wiretap e ingest).
- [[telepresence-modos-traffic-agent-sidecar-vs-node-agent]] — Veja também: Telepresence: escolha entre Traffic Agent como Sidecar injetado (padrão) ou Node-Agent sem reiniciar pods.
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
