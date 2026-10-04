---
id: software.devops.tranche09.000889
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

# Telepresence: depuração não-intrusiva com wiretap (cópia de tráfego) e ingest (apenas variáveis/volumes)

## Em uma frase
Os modos **`wiretap`** e **`ingest`** do Telepresence permitem depurar aplicações conectadas a um cluster sem nunca desviar ou interromper as respostas enviadas pelo pod remoto aos clientes reais do cluster.

## Por que importa
Em um ambiente de homologação integrada (onde testes automatizados de ponta a ponta estão rodando continuamente) ou ao investigar um bug difícil de reproduzir que só acontece com cargas reais de tráfego, usar `replace` ou `intercept` altera o caminho crítico da requisição — se o processo local do desenvolvedor estiver lento ou travar no debugger, o chamador receberá erro HTTP 500/timeout. Os modos `wiretap` e `ingest` documentados no README e na arquitetura v2.32 eliminam esse impacto.

## Como funciona
(1) **`telepresence wiretap <workload> --port <local>:<remota>`**: instrui o `Traffic Agent` a duplicar os pacotes/requisições de entrada que chegam ao serviço; o container original dentro do pod continua processando a requisição e devolvendo a resposta oficial ao cliente no cluster, enquanto uma **cópia idêntica** da requisição é enviada para a estação de trabalho do desenvolvedor (cujo retorno local é descartado pelo agente), permitindo colocar breakpoints no debugger local sem causar timeout no cluster; e (2) **`telepresence ingest <workload>`**: anexa-se ao container remoto exclusivamente para extrair suas variáveis de ambiente e montar seus volumes localmente, mantendo 100% do tráfego de entrada no pod remoto enquanto o processo local faz chamadas de saída pela VIF.

## Exemplo
```bash
# Receber uma cópia espelhada do tráfego em tempo real (wiretap) ou importar apenas ambiente e volumes (ingest)
telepresence wiretap catalog-service --port 8080:http
telepresence ingest catalog-service --env-file ./catalog.env
```

## Limites e trade-offs
Mesmo quando você usa `wiretap` (que descarta a resposta HTTP gerada pelo seu processo local) ou `ingest`, lembre-se de que **as chamadas de saída** feitas pelo seu processo local (como `INSERT`/`UPDATE` no banco de dados PostgreSQL do cluster ou publicação de mensagens em uma fila Kafka) são reais e chegarão aos serviços do cluster; portanto, tome cuidado com efeitos colaterais de escrita no banco ao processar requisições espelhadas por `wiretap`.

## Como verificar
Inicie um `telepresence wiretap`, pause o seu processo local em um breakpoint na IDE, faça uma requisição `curl` para o Service no cluster e confirme que o `curl` recebe resposta `200 OK` imediata do pod remoto enquanto sua IDE captura a requisição no breakpoint.

## Conexões
- [[telepresence-gerenciamento-traffic-manager-helm-namespaces-rbac]] — Veja também: Telepresence: instalação e administração do Traffic Manager no cluster (telepresence helm install/upgrade) e escopo de namespaces.
- [[telepresence-troubleshooting-logs-limpeza-sessoes-quit-uninstall]] — Veja também: Telepresence: diagnóstico de conectividade (gather-logs, loglevel) e limpeza de agentes e daemons (leave, uninstall, quit).
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.
- [[telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest]] — Referência cruzada direta com telepresence-quatro-modos-anexacao-replace-intercept-wiretap-ingest.
- [[mirrord-modos-trafego-mirror-vs-steal-filtragem-http]] — Referência cruzada direta com mirrord-modos-trafego-mirror-vs-steal-filtragem-http.

## Fontes
- [Telepresence GitHub — README.md (CNCF Local-to-Cluster Development, 4 Attachment Modes & Traffic Filtering)](https://raw.githubusercontent.com/telepresenceio/telepresence/release/v2/README.md) — README oficial do Telepresence (v2) detalhando eliminação do ciclo build/push/deploy, modos replace/intercept/wiretap/ingest, filtragem HTTP para equipes e importação de ambiente/volumes; consultado em 2026-10-03.
- [Telepresence Official Documentation — Architecture (User-Daemon, Root-Daemon VIF, Traffic Manager & Sidecar vs Node-Agent)](https://telepresence.io/docs/concepts/architecture) — Documentação oficial de arquitetura do Telepresence v2.32 explicando User-Daemon, Root-Daemon (Virtual Network Device VIF), Traffic Manager (telepresence helm install) e Traffic Agent como sidecar ou node-agent sem restart; consultado em 2026-10-03.
- [Telepresence — Official GitHub Repository](https://github.com/telepresenceio/telepresence) — Repositório oficial Apache-2.0 do Telepresence na CNCF; consultado em 2026-10-03.
