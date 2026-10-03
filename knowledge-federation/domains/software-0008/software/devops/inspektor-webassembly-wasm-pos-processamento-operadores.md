---
id: software.devops.tranche07.000634
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

# Inspektor Gadget: módulos WebAssembly (WASM) e arquitetura de Operadores customizáveis

## Em uma frase
O Inspektor Gadget utiliza uma arquitetura de Operadores (`operators`) reordenáveis e suporta módulos WebAssembly (WASM) embutidos nos Gadgets para pós-processar dados e estender a lógica em qualquer linguagem compatível com WASM.

## Por que importa
Embora os programas eBPF no kernel sejam ideais para coleta e filtragem ultrarrápida de eventos, o verificador do kernel Linux impõe restrições severas ao código eBPF (como limites de loops, ausência de ponto flutuante e manipulação complexa de strings ou formatação customizada). Segundo o README oficial do Inspektor Gadget, combinar eBPF no kernel com módulos WebAssembly no espaço de usuário permite pós-processar eventos e customizar operadores com segurança e portabilidade dentro da mesma imagem OCI do Gadget.

## Como funciona
No Inspektor Gadget, um **operador** (`operator`) é qualquer componente do framework onde uma ação é executada sobre o ciclo de vida ou sobre os dados de um Gadget. Alguns operadores atuam nos bastidores (como buscar a imagem OCI e carregar os programas eBPF no kernel), enquanto outros são expostos ao usuário (como enriquecimento Kubernetes/container, filtragem, ordenação, exportação para OpenTelemetry/Prometheus e execução WASM) e podem ter sua ordem de execução alterada ou sobrescrita. Quando um Gadget inclui um módulo `.wasm`, o operador WASM executa esse bytecode em um sandbox isolado em user-space para transformar campos, agregar estatísticas complexas ou validar regras antes da exibição ou exportação dos dados.

## Exemplo
```bash
# Executar um Gadget inspecionando os parâmetros expostos pelos diferentes operadores ativos (--help)
kubectl gadget run trace_open:latest --help
```

## Limites e trade-offs
O pós-processamento em WebAssembly ocorre no espaço de usuário após os eventos terem atravessado o ring buffer ou perf buffer do kernel; portanto, o módulo WASM não substitui a filtragem primária em eBPF: se milhões de eventos irrelevantes forem enviados do kernel para serem descartados apenas dentro do módulo WASM, haverá desperdício significativo de CPU e troca de contexto.

## Como verificar
Inspecione a saída de `kubectl gadget run <gadget>:latest --help` para verificar a lista de flags injetadas dinamicamente por cada operador habilitado (como `oci`, `ebpf`, `kubeipresolver`, `kubemanager`, `wasm`, `cli`).

## Conexões
- [[inspektor-enriquecimento-kernel-kubernetes-filtragem-ebpf]] — Veja também: Inspektor Gadget: enriquecimento bidirecional de metadados Kubernetes e filtragem in-kernel de alto desempenho.
- [[inspektor-modos-operacao-kubectl-gadget-ig-linux-gadgetctl]] — Veja também: Inspektor Gadget: modos de operação com kubectl-gadget, binário ig, kubectl debug node e cliente remoto gadgetctl.
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Referência cruzada direta com inspektor-framework-ebpf-inspecao-kubernetes-linux.
- [[inspektor-gadgets-imagens-oci-build-artifact-hub]] — Referência cruzada direta com inspektor-gadgets-imagens-oci-build-artifact-hub.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
