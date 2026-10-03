---
id: software.devops.tranche07.000638
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

# Inspektor Gadget: verificação de assinaturas de imagens OCI, SBOMs e restrição de Gadgets permitidos

## Em uma frase
O Inspektor Gadget fornece mecanismos de segurança para verificar assinaturas criptográficas das imagens OCI de Gadgets, publicar SBOMs de releases e restringir quais Gadgets podem ser executados no cluster ou host.

## Por que importa
Como um Gadget contém bytecode eBPF que será executado com privilégios de kernel em todos os nós do cluster Kubernetes, permitir que qualquer usuário com permissão de execução rode uma imagem OCI arbitrária da internet criaria um vetor crítico de comprometimento de infraestrutura. De acordo com a seção `Security features` do README oficial do Inspektor Gadget, o projeto integra verificação de ativos (`Verify assets`) e políticas de restrição (`Restricting Gadgets`) para trancar a superfície de execução.

## Como funciona
Por padrão, o Inspektor Gadget verifica a autenticidade das imagens OCI de Gadgets utilizando assinaturas criptográficas (Cosign / chaves públicas oficiais) antes de carregar qualquer programa eBPF no kernel, recusando imagens não assinadas ou adulteradas a menos que a verificação seja explicitamente desabilitada. Além disso, os administradores que implantam o DaemonSet (`kubectl gadget deploy`) ou o `ig daemon` podem configurar filtros de restrição para bloquear ou permitir apenas repositórios, registries ou digests específicos de Gadgets, e todas as releases oficiais do projeto são acompanhadas de arquivos SBOM (Software Bill of Materials, como `ig-linux-amd64-*.bom.json`) para auditoria de cadeia de suprimentos.

## Exemplo
```bash
# Implantar o Inspektor Gadget no Kubernetes mantendo a verificação de assinatura de imagens OCI ativa
kubectl gadget deploy --verify-image=true
```

## Limites e trade-offs
Ao construir Gadgets customizados internos com `ig image build` para uso em produção, a equipe de plataforma precisa assinar suas próprias imagens OCI com Cosign e fornecer a chave pública correspondente na configuração do Inspektor Gadget (`--public-keys`), caso contrário o daemon rejeitará a imagem customizada durante a validação de assinatura.

## Como verificar
Tente executar uma imagem de Gadget não assinada com a verificação padrão ativa e confirme que o Inspektor Gadget aborta o carregamento do programa eBPF exibindo erro de falha na verificação de assinatura.

## Conexões
- [[inspektor-exportacao-telemetria-opentelemetry-prometheus-declarativa]] — Veja também: Inspektor Gadget: coleta e exportação declarativa de métricas e logs eBPF para OpenTelemetry e Prometheus.
- [[inspektor-requisitos-kernel-linux-btf-core-cilium-ebpf]] — Veja também: Inspektor Gadget: requisitos de kernel Linux (>= 5.10), BTF (BPF Type Format) e biblioteca cilium/ebpf.
- [[inspektor-framework-ebpf-inspecao-kubernetes-linux]] — Referência cruzada direta com inspektor-framework-ebpf-inspecao-kubernetes-linux.
- [[inspektor-gadgets-imagens-oci-build-artifact-hub]] — Referência cruzada direta com inspektor-gadgets-imagens-oci-build-artifact-hub.
- [[kubescape-monitoramento-runtime-ebpf-network-policies-prometheus]] — Referência cruzada direta com kubescape-monitoramento-runtime-ebpf-network-policies-prometheus.

## Fontes
- [Inspektor Gadget GitHub — README.md (OCI Gadgets, Enrichment, WASM & Operations)](https://raw.githubusercontent.com/inspektor-gadget/inspektor-gadget/main/README.md) — README oficial do Inspektor Gadget detalhando empacotamento de programas eBPF em imagens OCI, enriquecimento bidirecional Kubernetes, módulos WebAssembly, operadores e requisitos de kernel Linux >= 5.10 com BTF; consultado em 2026-10-03.
- [Inspektor Gadget Official Documentation — Gadgets Catalog & Reference](https://www.inspektor-gadget.io/docs/latest/gadgets/) — Documentação oficial dos Gadgets (trace, top, snapshot, profile) e modos de execução com kubectl-gadget, ig e gadgetctl; consultado em 2026-10-03.
- [Inspektor Gadget — Official GitHub Repository](https://github.com/inspektor-gadget/inspektor-gadget) — Repositório oficial do Inspektor Gadget na CNCF; consultado em 2026-10-03.
