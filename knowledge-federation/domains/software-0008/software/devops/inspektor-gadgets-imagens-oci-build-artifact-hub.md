---
id: software.devops.tranche07.000632
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

# Inspektor Gadget: empacotamento de programas eBPF em imagens OCI (Gadgets) e distribuição via Artifact Hub

## Em uma frase
No Inspektor Gadget, um Gadget é uma imagem OCI padrão que encapsula um ou mais programas eBPF, um arquivo YAML de metadados e, opcionalmente, módulos WebAssembly (WASM) para pós-processamento.

## Por que importa
Historicamente, distribuir ferramentas eBPF exigia compilar código C no próprio servidor alvo com cabeçalhos do kernel instalados (como nas ferramentas BCC clássicas) ou atualizar todo o binário do agente sempre que um novo script de rastreamento era criado. De acordo com a documentação oficial do Inspektor Gadget (introduzida a partir da v0.31.0 com image-based gadgets), empacotar programas eBPF como imagens OCI permite armazená-los, versioná-los e assiná-los em qualquer registry de containers compatível com a especificação OCI, além de compartilhá-los no Artifact Hub.

## Como funciona
Um desenvolvedor escreve o código eBPF em C (utilizando BTF e CO-RE) e define um arquivo de metadados YAML descrevendo os mapas, campos, parâmetros e operadores associados; em seguida, executa o comando `ig image build` para compilar o bytecode eBPF (e eventual módulo WASM) e empacotá-lo em camadas de uma imagem OCI. O artefato resultante pode ser enviado via `ig image push` para registries como GHCR, Docker Hub ou registries privados e executado em qualquer nó Linux ou cluster Kubernetes simplesmente referenciando sua tag (por exemplo, `trace_open:latest` ou `ghcr.io/inspektor-gadget/gadget/trace_dns:latest`).

## Exemplo
```bash
# Construir uma imagem OCI de um Gadget a partir do diretório local e listar imagens locais com o binário ig
sudo ig image build -t meu-registry.local/gadgets/trace_custom:v1 .
sudo ig image list

# Executar um Gadget diretamente a partir de sua imagem OCI
sudo ig run trace_open:latest
```

## Limites e trade-offs
Como a execução de uma imagem OCI de Gadget envolve carregar bytecode eBPF diretamente no kernel do nó, puxar imagens de registries externos não confiáveis sem verificação representa um risco severo de segurança; por isso, em ambientes de produção, é essencial habilitar os mecanismos de verificação de assinatura de imagens e restrição de Gadgets permitidos do Inspektor Gadget.

## Como verificar
Execute `sudo ig image list` ou `sudo ig image inspect trace_open:latest` para verificar as camadas da imagem OCI do Gadget (bytecode eBPF, metadados e digest SHA-256).

## Conexões
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Veja também: Inspektor Gadget: conjunto de ferramentas e framework eBPF para inspeção em Kubernetes e Linux.
- [[inspektor-enriquecimento-kernel-kubernetes-filtragem-ebpf]] — Veja também: Inspektor Gadget: enriquecimento bidirecional de metadados Kubernetes e filtragem in-kernel de alto desempenho.
- [[inspektor-webassembly-wasm-pos-processamento-operadores]] — Referência cruzada direta com inspektor-webassembly-wasm-pos-processamento-operadores.
- [[inspektor-seguranca-verificacao-assinaturas-sbom-restricao-gadgets]] — Referência cruzada direta com inspektor-seguranca-verificacao-assinaturas-sbom-restricao-gadgets.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
