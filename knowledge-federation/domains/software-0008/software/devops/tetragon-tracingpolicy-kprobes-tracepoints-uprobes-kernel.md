---
id: software.devops.tranche07.000623
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
fontes: ["https://raw.githubusercontent.com/cilium/tetragon/main/README.md", "https://tetragon.io/docs/overview/", "https://github.com/cilium/tetragon"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cilium Tetragon: CRD TracingPolicy e rastreamento genérico com kprobes, tracepoints e uprobes

## Em uma frase
O recurso customizado `TracingPolicy` (e `TracingPolicyNamespaced`) do Cilium Tetragon permite instrumentar dinamicamente qualquer função do kernel (`process_kprobe`), tracepoint (`process_tracepoint`) ou função de usuário (`process_uprobe`) sem recompilar o agente.

## Por que importa
Nenhuma ferramenta de segurança consegue prever ou codificar estaticamente todas as funções do kernel que diferentes equipes precisarão monitorar para casos de uso específicos de rede, arquivos, criptografia ou chamadas internas. Segundo a documentação oficial do Tetragon (`Overview`), nada sobre quais funções são rastreadas ou quais filtros são aplicados está engessado no motor: os usuários definem políticas declarativas `TracingPolicy` que engancham profundamente em estruturas do kernel onde aplicações em user space não conseguem manipular nem falsificar os argumentos.

## Como funciona
Quando um manifesto `TracingPolicy` (escopo de cluster) ou `TracingPolicyNamespaced` (restrito a um namespace Kubernetes) é aplicado na API do Kubernetes, o operador/agente do Tetragon compila e anexa os sensores eBPF correspondentes aos seletores definidos (`kprobes`, `tracepoints`, `uprobes` ou `lsm`). Na especificação da política, o administrador declara a função alvo (por exemplo, `tcp_connect`, `security_file_permission` ou `sys_enter`), os tipos dos argumentos do kernel que devem ser extraídos (como `sock`, `file`, `int`, `char_buf`) e os seletores (`selectors`) que filtram no próprio eBPF por `matchPIDs`, `matchArgs`, `matchBinaries`, `matchCapabilities` ou `matchNamespaces` antes de emitir eventos `process_kprobe`, `process_tracepoint` ou `process_uprobe`.

## Exemplo
```yaml
# Exemplo de TracingPolicyNamespaced monitorando chamadas tcp_connect no kernel via kprobe
apiVersion: cilium.io/v1alpha1
kind: TracingPolicyNamespaced
metadata:
  name: monitor-conexoes-tcp
  namespace: producao
spec:
  kprobes:
    - call: "tcp_connect"
      syscall: false
      args:
        - index: 0
          type: "sock"
```

## Limites e trade-offs
Enganchar `kprobes` em funções internas do kernel que são executadas milhões de vezes por segundo (como funções de leitura/escrita de pacotes ou alocação de páginas) sem especificar seletores restritivos (`matchArgs`, `matchBinaries` ou `podSelector`) no eBPF pode introduzir latência mensurável nas chamadas de sistema do nó; além disso, assinaturas de funções internas do kernel (`kprobes` não-syscall) podem variar entre versões principais do kernel Linux.

## Como verificar
Aplique a `TracingPolicy` com `kubectl apply -f policy.yaml`, liste as políticas carregadas no agente com `tetra tracingpolicy list` e verifique a geração de eventos `process_kprobe` quando o workload realiza a operação monitorada.

## Conexões
- [[tetragon-ciclo-vida-processos-process-exec-exit-arvore]] — Veja também: Cilium Tetragon: observabilidade completa do ciclo de vida de processos com process_exec e process_exit.
- [[tetragon-enforcement-kernel-sigkill-override-bloqueio-tempo-real]] — Veja também: Cilium Tetragon: runtime enforcement síncrono no kernel com ações Sigkill e Override.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.
- [[tetragon-monitoramento-arquivos-credenciais-execucao-privilegiada]] — Referência cruzada direta com tetragon-monitoramento-arquivos-credenciais-execucao-privilegiada.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
