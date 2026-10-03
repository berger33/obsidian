---
id: software.devops.tranche07.000640
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
fontes: ["https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md", "https://raw.githubusercontent.com/kubescape/kubescape/master/README.md", "https://github.com/inspektor-gadget/inspektor-gadget"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Inspektor Gadget: uso como biblioteca Golang embarcável e integração de runtime no ecossistema CNCF

## Em uma frase
Além de suas CLIs (`kubectl-gadget`, `ig`, `gadgetctl`), o Inspektor Gadget expõe pacotes Golang embarcáveis que permitem a plataformas de segurança da CNCF (como o Kubescape) integrar inspeção eBPF de runtime diretamente em seus operadores.

## Por que importa
Construir do zero um motor de coleta eBPF capaz de carregar imagens OCI, realizar relocações BTF, gerenciar operadores e enriquecer eventos com metadados de container runtimes e Kubernetes exige anos de engenharia especializada de kernel. Conforme documentado no README oficial do Inspektor Gadget (`Code examples`) e no README do Kubescape, o Inspektor Gadget foi projetado como um framework modular cujos pacotes Go podem ser importados diretamente por outras ferramentas cloud-native.

## Como funciona
A arquitetura interna do Inspektor Gadget separa claramente o runtime de execução de Gadgets, o registro de operadores (como enriquecimento de containers/Kubernetes e gerenciamento de imagens OCI) e a camada de apresentação CLI. Desenvolvedores Go podem importar os pacotes de `github.com/inspektor-gadget/inspektor-gadget/pkg/...` (conforme demonstrado no diretório `/examples/` do repositório) para instanciar o runtime programaticamente, carregar Gadgets específicos no kernel e consumir os callbacks de eventos estruturados em structs Go dentro de seu próprio agente — exatamente como o operador in-cluster do Kubescape faz para monitorar chamadas de sistema, processos e tráfego de rede em tempo real para detecção de ameaças e geração de NetworkPolicies.

## Exemplo
```bash
# Inspecionar a documentação dos pacotes Go exportados pelo Inspektor Gadget
go doc github.com/inspektor-gadget/inspektor-gadget/pkg/gadget-context
```

## Limites e trade-offs
Embarcar o Inspektor Gadget como biblioteca Golang dentro de outro operador Kubernetes significa que o binário hospedeiro passa a herdar os mesmos requisitos de privilégios de sistema (capabilities `CAP_BPF`, `CAP_PERFMON`, `CAP_SYS_ADMIN` ou container privilegiado, acesso ao `/sys/kernel/btf` e ao socket do container runtime) necessários para carregar programas eBPF e enriquecer containers no nó.

## Como verificar
Consulte os exemplos oficiais na pasta `examples/` do repositório `inspektor-gadget/inspektor-gadget` e verifique como operadores integrados (como o `node-agent` do Kubescape) carregam sensores eBPF usando o framework do Inspektor Gadget.

## Conexões
- [[inspektor-requisitos-kernel-linux-btf-core-cilium-ebpf]] — Veja também: Inspektor Gadget: requisitos de kernel Linux (>= 5.10), BTF (BPF Type Format) e biblioteca cilium/ebpf.
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Referência cruzada direta com inspektor-framework-ebpf-inspecao-kubernetes-linux.
- [[inspektor-webassembly-wasm-pos-processamento-operadores]] — Referência cruzada direta com inspektor-webassembly-wasm-pos-processamento-operadores.
- [[kubescape-monitoramento-runtime-ebpf-network-policies-prometheus]] — Referência cruzada direta com kubescape-monitoramento-runtime-ebpf-network-policies-prometheus.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
