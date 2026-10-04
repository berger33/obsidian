---
id: software.devops.tranche07.000635
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md", "https://www.inspektor-gadget.io/docs/latest/gadgets/", "https://github.com/inspektor-gadget/inspektor-gadget"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Inspektor Gadget: modos de operação com kubectl-gadget, binário ig, kubectl debug node e cliente remoto gadgetctl

## Em uma frase
O Inspektor Gadget opera em múltiplos modos: cluster-wide via `kubectl gadget`, localmente em Linux/containers via `ig`, sem instalação prévia no cluster via `kubectl debug node`, como daemon remoto com `gadgetctl` (macOS/Windows) ou como biblioteca Go.

## Por que importa
Diferentes cenários de resposta a incidentes impõem restrições distintas: em alguns clusters o DaemonSet do Inspektor Gadget já está instalado; em outros clusters de produção trancados não é permitido instalar um DaemonSet permanente, mas o engenheiro precisa depurar um nó específico imediatamente; ou ainda um desenvolvedor em macOS/Windows precisa inspecionar uma VM Linux remota. O README oficial do Inspektor Gadget documenta cada um desses modos de operação.

## Como funciona
(1) No modo Kubernetes implantado, `kubectl gadget deploy` instala o DaemonSet no cluster e `kubectl gadget run` coordena a execução em todos os nós simultaneamente. (2) Para depurar um nó Kubernetes sem instalar o Inspektor Gadget no cluster, usa-se `kubectl debug --profile=sysadmin node/<nome-do-no> -ti --image=ghcr.io/inspektor-gadget/ig:latest -- ig run <gadget>`. (3) Em servidores Linux, o binário `ig` pode ser instalado em `/usr/local/bin/ig` ou executado em um container Docker privilegiado (`--privileged -v /:/host --pid=host`). (4) Para controle remoto a partir de macOS ou Windows, inicia-se `sudo ig daemon --host=tcp://0.0.0.0:1234` na máquina Linux e conecta-se com o binário cliente `gadgetctl run <gadget> --remote-address=tcp://$IP:1234`.

## Exemplo
```bash
# Modo sem instalação prévia em Kubernetes usando kubectl debug em um nó específico
kubectl debug --profile=sysadmin node/worker-node-01 -ti \
  --image=ghcr.io/inspektor-gadget/ig:latest -- ig run trace_open:latest

# Modo container Docker direto em um host Linux
docker run -ti --rm --privileged -v /:/host --pid=host \
  ghcr.io/inspektor-gadget/ig:latest run trace_open:latest
```

## Limites e trade-offs
Executar `sudo ig daemon --tls-insecure --host=tcp://0.0.0.0:1234` conforme o exemplo básico de quickstart expõe um endpoint TCP sem autenticação mTLS capaz de carregar programas eBPF no kernel da máquina Linux; portanto, a flag `--tls-insecure` só deve ser usada em redes locais de laboratório isoladas, exigindo certificados TLS ou túnel SSH/socket UNIX em ambientes reais.

## Como verificar
Teste a execução local com `sudo ig version` (ou `kubectl gadget version`) e valide que o comando `run trace_open:latest` coleta eventos do kernel e encerra limpando os programas eBPF ao receber `Ctrl+C`.

## Conexões
- [[inspektor-webassembly-wasm-pos-processamento-operadores]] — Veja também: Inspektor Gadget: módulos WebAssembly (WASM) e arquitetura de Operadores customizáveis.
- [[inspektor-catalogo-gadgets-trace-top-snapshot-profile]] — Veja também: Inspektor Gadget: catálogo de Gadgets para rastreamento (trace), top consumidores, snapshots e profiling.
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Referência cruzada direta com inspektor-framework-ebpf-inspecao-kubernetes-linux.
- [[inspektor-gadgets-imagens-oci-build-artifact-hub]] — Referência cruzada direta com inspektor-gadgets-imagens-oci-build-artifact-hub.
- [[tetragon-implantacao-kubernetes-linux-docker-standalone]] — Referência cruzada direta com tetragon-implantacao-kubernetes-linux-docker-standalone.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
