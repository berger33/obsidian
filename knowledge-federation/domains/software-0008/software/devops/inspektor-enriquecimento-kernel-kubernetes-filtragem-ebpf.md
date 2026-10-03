---
id: software.devops.tranche07.000633
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

# Inspektor Gadget: enriquecimento bidirecional de metadados Kubernetes e filtragem in-kernel de alto desempenho

## Em uma frase
O Inspektor Gadget realiza enriquecimento bidirecional: traduz primitivas de baixo nível do kernel (mount namespaces, PIDs) em conceitos do Kubernetes (pods, containers, DNS) na saída e converte filtros de alto nível em filtros in-kernel no eBPF.

## Por que importa
Os dados coletados pelo eBPF dentro do kernel Linux não possuem nenhum conhecimento nativo sobre abstrações de espaço de usuário como nomes de pods Kubernetes, namespaces, labels ou nomes de containers do runtime. Conforme detalhado na seção `What is enrichment?` do README oficial do Inspektor Gadget, o enriquecimento automático torna a telemetria eBPF imediatamente compreensível para operadores e permite filtrar eventos de alta frequência diretamente no kernel usando apenas nomes de pods ou containers.

## Como funciona
Quando um programa eBPF captura um evento (como a abertura de um arquivo ou um pacote de rede), ele registra primitivas do kernel como o ID do mount namespace (`mntns_id`), o net namespace (`netns_id`) ou o PID. No caminho de saída (kernel para usuário), o operador de enriquecimento do Inspektor Gadget cruza esses identificadores com o estado do container runtime (containerd, CRI-O, Docker) e da API do Kubernetes para anexar `k8s.namespace`, `k8s.podName`, `k8s.containerName` e nomes DNS. No caminho inverso (usuário para kernel), quando o operador executa um Gadget filtrando por `--podname meu-pod` ou `-n producao`, o Inspektor Gadget resolve previamente esse pod para o `mntns_id` ou `netns_id` correspondente e popula um mapa eBPF no kernel, descartando eventos de todos os outros containers antes mesmo que saiam do espaço de kernel.

## Exemplo
```bash
# Executar o Gadget trace_open no Kubernetes filtrando in-kernel apenas por um namespace e pod específicos
kubectl gadget run trace_open:latest \
  --namespace producao \
  --podname api-checkout-7d9b8c-x2k9p
```

## Limites e trade-offs
O enriquecimento automático requer que o daemon do Inspektor Gadget tenha acesso ao socket do container runtime local (CRI) e metadados de pods do nó; se o socket do runtime estiver configurado em um caminho não padrão no nó Kubernetes e não for informado na implantação do `kubectl gadget deploy`, o enriquecimento não conseguirá resolver os `mntns_id` e os campos de container/pod aparecerão vazios.

## Como verificar
Execute `kubectl gadget run trace_open:latest -A` em um cluster de teste e confirme que as colunas `K8S.NAMESPACE`, `K8S.PODNAME` e `K8S.CONTAINERNAME` são preenchidas automaticamente para cada evento de abertura de arquivo.

## Conexões
- [[inspektor-gadgets-imagens-oci-build-artifact-hub]] — Veja também: Inspektor Gadget: empacotamento de programas eBPF em imagens OCI (Gadgets) e distribuição via Artifact Hub.
- [[inspektor-webassembly-wasm-pos-processamento-operadores]] — Veja também: Inspektor Gadget: módulos WebAssembly (WASM) e arquitetura de Operadores customizáveis.
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Referência cruzada direta com inspektor-framework-ebpf-inspecao-kubernetes-linux.
- [[tetragon-consciencia-kubernetes-identidades-pods-namespaces]] — Referência cruzada direta com tetragon-consciencia-kubernetes-identidades-pods-namespaces.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
