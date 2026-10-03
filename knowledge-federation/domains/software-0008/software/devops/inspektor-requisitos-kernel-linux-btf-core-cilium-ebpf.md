---
id: software.devops.tranche07.000639
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

# Inspektor Gadget: requisitos de kernel Linux (>= 5.10), BTF (BPF Type Format) e biblioteca cilium/ebpf

## Em uma frase
Os Gadgets desenvolvidos pelo projeto Inspektor Gadget exigem pelo menos o kernel Linux 5.10 com BTF (BPF Type Format) habilitado e utilizam a biblioteca `cilium/ebpf` em Go para carregar e gerenciar programas CO-RE.

## Por que importa
No passado, ferramentas baseadas em eBPF precisavam instalar o compilador Clang/LLVM e os pacotes `linux-headers` exatos da distribuição em cada nó Kubernetes de produção para compilar o código BPF em tempo de execução, aumentando o tamanho das imagens em centenas de megabytes e o consumo de CPU/memória na inicialização. Segundo a seção `Kernel requirements` e `Thanks` do README oficial do Inspektor Gadget, o uso de BTF e da biblioteca `cilium/ebpf` permite distribuir binários eBPF pré-compilados leves e portáveis.

## Como funciona
Quando o kernel Linux é compilado com `CONFIG_DEBUG_INFO_BTF=y` (disponível por padrão na maioria das distribuições com Linux >= 5.10), ele expõe em `/sys/kernel/btf/vmlinux` a descrição compacta de todas as estruturas de dados e tipos internos daquele kernel exato. Quando o Inspektor Gadget baixa a imagem OCI de um Gadget, o gerenciador em espaço de usuário (construído sobre a biblioteca `cilium/ebpf` em Go) lê o arquivo BTF do kernel local e aplica automaticamente as relocações de offsets de campos (CO-RE) no bytecode eBPF antes de enviá-lo à chamada de sistema `bpf()`, garantindo compatibilidade entre diferentes versões de kernel sem compilador local.

## Exemplo
```bash
# Verificar no nó Linux se o kernel atende ao requisito >= 5.10 e se o arquivo BTF vmlinux está disponível
uname -r
ls -lh /sys/kernel/btf/vmlinux
```

## Limites e trade-offs
Embora o requisito base dos Gadgets oficiais seja Linux 5.10 com BTF, Gadgets específicos que utilizam recursos mais recentes do subsistema eBPF (como iteradores BPF avançados, kfuncs ou hooks específicos de rede/segurança) podem exigir versões de kernel ainda mais novas; se o kernel do nó não suportar o tipo de programa (`prog_type`) ou helper exigido pelo Gadget, o verificador do kernel recusará o carregamento naquele nó.

## Como verificar
Confirme a existência de `/sys/kernel/btf/vmlinux` nos nós do cluster Kubernetes e execute um Gadget básico como `trace_open:latest` para validar o carregamento CO-RE via `cilium/ebpf`.

## Conexões
- [[inspektor-seguranca-verificacao-assinaturas-sbom-restricao-gadgets]] — Veja também: Inspektor Gadget: verificação de assinaturas de imagens OCI, SBOMs e restrição de Gadgets permitidos.
- [[inspektor-integracao-biblioteca-golang-kubescape-ecossistema]] — Veja também: Inspektor Gadget: uso como biblioteca Golang embarcável e integração de runtime no ecossistema CNCF.
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Referência cruzada direta com inspektor-framework-ebpf-inspecao-kubernetes-linux.
- [[inspektor-gadgets-imagens-oci-build-artifact-hub]] — Referência cruzada direta com inspektor-gadgets-imagens-oci-build-artifact-hub.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
