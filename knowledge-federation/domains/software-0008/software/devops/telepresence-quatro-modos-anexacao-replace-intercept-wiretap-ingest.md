---
id: software.devops.tranche09.000882
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

# Telepresence: os 4 modos de anexação a workloads (replace, intercept, wiretap e ingest)

## Em uma frase
O Telepresence oferece quatro modos distintos para conectar seu processo local a um workload no cluster: **replace** (substitui o container remoto), **intercept** (intercepta uma porta de serviço), **wiretap** (recebe uma cópia do tráfego sem interferir) e **ingest** (importa apenas variáveis de ambiente e volumes sem redirecionar tráfego de entrada).

## Por que importa
Nem toda sessão de desenvolvimento tem o mesmo objetivo: às vezes o desenvolvedor quer apenas rodar um consumidor local ou script com as variáveis e segredos do pod sem roubar tráfego HTTP (`ingest`); às vezes quer inspecionar requisições reais de produção sem afetar a resposta dada ao usuário (`wiretap`); e às vezes quer substituir completamente o container remoto pelo seu código local (`replace` ou `intercept`). A seção `Key Features` do README oficial e a arquitetura v2.32 detalham os quatro modos.

## Como funciona
Quando o `User-Daemon` solicita uma anexação ao `Traffic Manager` e ao `Traffic Agent`: (1) **`replace`**: substitui o container de aplicação remoto no pod e roteia todo o tráfego destinado àquele container para a estação de trabalho; (2) **`intercept`**: intercepta tráfego de uma porta de Service específica (todo o tráfego ou apenas requisições filtradas por HTTP header/path) para a porta local do desenvolvedor, mantendo o container remoto ativo para as demais requisições; (3) **`wiretap`**: o `Traffic Agent` envia uma **cópia** espelhada das requisições de entrada para a estação de trabalho enquanto o container no pod continua respondendo normalmente; e (4) **`ingest`**: não altera o tráfego de entrada do pod, apenas disponibiliza as variáveis de ambiente e os volumes montados do container remoto para o processo local.

## Exemplo
```bash
# Interceptar o tráfego do deployment checkout-service redirecionando para a porta 8080 da máquina local
telepresence intercept checkout-service --port 8080:http
telepresence list
telepresence leave checkout-service
```

## Limites e trade-offs
Usar `replace` ou um `intercept` global (sem filtro de cabeçalho HTTP) em um cluster de staging compartilhado por toda a equipe fará com que **todas** as requisições enviadas por outros desenvolvedores ou testes de QA para aquele serviço caiam no seu laptop local (e falhem se o seu debugger estiver pausado em um breakpoint); em clusters compartilhados, prefira `intercept` com filtros HTTP, `wiretap` ou `ingest`.

## Como verificar
Execute `telepresence list` para verificar qual modo (`intercepted`, `replaced`, `wiretapped` ou `ingested`) está ativo em cada deployment do namespace.

## Conexões
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Veja também: Telepresence: desenvolvimento local conectado a clusters Kubernetes remotos sem ciclo build/push/deploy.
- [[telepresence-filtragem-trafego-http-headers-paths-equipes]] — Veja também: Telepresence: interceptações seletivas por cabeçalho HTTP (--http-header) e caminho (--http-path-*) em clusters compartilhados.
- [[telepresence-modos-traffic-agent-sidecar-vs-node-agent]] — Referência cruzada direta com telepresence-modos-traffic-agent-sidecar-vs-node-agent.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
