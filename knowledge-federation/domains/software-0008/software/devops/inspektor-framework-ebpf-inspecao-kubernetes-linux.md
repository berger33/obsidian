---
id: software.devops.tranche07.000631
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

# Inspektor Gadget: conjunto de ferramentas e framework eBPF para inspeção em Kubernetes e Linux

## Em uma frase
O Inspektor Gadget (licenciado sob Apache-2.0 para user-space e GPL-2.0 para templates BPF) é um conjunto de ferramentas e framework para coleta de dados e inspeção de sistemas em clusters Kubernetes e hosts Linux usando eBPF.

## Por que importa
Diagnosticar problemas complexos de baixo nível em clusters Kubernetes — como falhas intermitentes de resolução DNS, arquivos abertos por containers efêmeros, drops de pacotes TCP ou chamadas de sistema bloqueadas — usando ferramentas tradicionais de Linux exige instalar pacotes de depuração em cada nó e traduzir manualmente números de PID e inodes para nomes de pods. Segundo o README oficial do Inspektor Gadget, o projeto gerencia o empacotamento, a implantação e a execução de programas eBPF encapsulados em imagens OCI (chamados Gadgets), enriquecendo automaticamente os dados do kernel com recursos de alto nível do Kubernetes.

## Como funciona
O Inspektor Gadget fornece uma arquitetura modular que opera tanto em clusters Kubernetes (através do plugin `kubectl-gadget` e de um DaemonSet no cluster) quanto diretamente em hosts Linux e containers (via binário `ig`), além de permitir controle remoto a partir de macOS ou Windows via `gadgetctl` ou incorporação direta como biblioteca Golang. Para executar os Gadgets oficiais desenvolvidos pelo projeto, o nó hospedeiro precisa rodar pelo menos o kernel Linux 5.10 com suporte a BTF (BPF Type Format) habilitado, permitindo que os programas eBPF sejam compilados uma vez (CO-RE — Compile Once – Run Everywhere) e carregados com segurança em diferentes versões de kernel.

## Exemplo
```bash
# Instalação do plugin kubectl-gadget via krew, implantação no cluster e execução do Gadget trace_open
kubectl krew install gadget
kubectl gadget deploy
kubectl gadget run trace_open:latest
```

## Limites e trade-offs
Como os Gadgets carregam programas eBPF diretamente no kernel Linux do nó hospedeiro, o DaemonSet do Inspektor Gadget no Kubernetes (ou a execução do binário `ig` no Linux) requer privilégios elevados (`sudo` / container `--privileged`) e um kernel >= 5.10 com BTF habilitado; em nós com kernels antigos sem BTF, os Gadgets baseados em CO-RE não poderão ser carregados sem suporte específico.

## Como verificar
Após executar `kubectl gadget deploy`, verifique se os pods do DaemonSet `gadget` estão `Running` no namespace `gadget` e execute `kubectl gadget version` para confirmar que cliente e servidor estão sincronizados.

## Conexões
- [[inspektor-gadgets-imagens-oci-build-artifact-hub]] — Veja também: Inspektor Gadget: empacotamento de programas eBPF em imagens OCI (Gadgets) e distribuição via Artifact Hub.
- [[inspektor-enriquecimento-kernel-kubernetes-filtragem-ebpf]] — Referência cruzada direta com inspektor-enriquecimento-kernel-kubernetes-filtragem-ebpf.
- [[inspektor-modos-operacao-kubectl-gadget-ig-linux-gadgetctl]] — Referência cruzada direta com inspektor-modos-operacao-kubectl-gadget-ig-linux-gadgetctl.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
