---
id: software.devops.tranche07.000624
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

# Cilium Tetragon: runtime enforcement síncrono no kernel com ações Sigkill e Override

## Em uma frase
O Cilium Tetragon executa aplicação de políticas de segurança (runtime enforcement) diretamente no kernel via eBPF, permitindo encerrar processos (`Sigkill`) ou sobrescrever o retorno de funções (`Override`) antes que a operação seja concluída.

## Por que importa
Em arquiteturas de segurança reativas baseadas em agentes de espaço de usuário, quando o evento de uma escalada de privilégio ou leitura de segredo chega ao agente externo para análise, o atacante já concluiu a syscall e pode ter exfiltrado os dados pela rede. Conforme a documentação oficial do Tetragon (`eBPF Kernel Aware`), executar a política dentro do kernel permite matar o processo ou bloquear a chamada no exato instante da violação, antes que o processo tenha chance de concluir a syscall ou executar instruções adicionais.

## Como funciona
Dentro dos seletores (`selectors`) de uma `TracingPolicy`, além de filtrar argumentos e metadados de processo/Kubernetes no eBPF, o administrador pode configurar `matchActions`. A ação `Sigkill` instrui o programa eBPF no kernel a enviar imediatamente um sinal `SIGKILL` não-ignorável ao processo atual assim que a condição da regra é satisfeita na função monitorada. Já a ação `Override` (utilizada em conjunto com `fmod_ret` / error injection em funções de segurança ou syscalls suportadas pelo kernel) altera o valor de retorno da função para um código de erro POSIX (como `-EPERM` / `-1`), negando a operação específica sem necessariamente derrubar o processo inteiro.

## Exemplo
```yaml
# Trecho de TracingPolicy que bloqueia e encerra processos que tentem modificar /etc/passwd em um pod
apiVersion: cilium.io/v1alpha1
kind: TracingPolicyNamespaced
metadata:
  name: bloquear-escrita-etc-passwd
  namespace: default
spec:
  kprobes:
    - call: "security_file_permission"
      syscall: false
      args:
        - index: 0
          type: "file"
        - index: 1
          type: "int"
      selectors:
        - matchArgs:
            - index: 0
              operator: "Equal"
              values:
                - "/etc/passwd"
            - index: 1
              operator: "Equal"
              values:
                - "2" # MAY_WRITE
          matchActions:
            - action: Sigkill
```

## Limites e trade-offs
A ação `Sigkill` termina abruptamente o processo infrator no kernel (resultando em saída `Killed` / código 137), o que pode derrubar todo o container se o processo atingido for o PID 1 da aplicação; por isso, recomenda-se sempre validar novas políticas inicialmente apenas com a ação padrão `Post` (emissão de evento de observabilidade) e auditar falsos positivos antes de ativar `Sigkill` ou `Override` em produção.

## Como verificar
Em um ambiente de homologação, aplique a política com `matchActions` e tente executar a ação proibida dentro de um pod de teste, verificando que o comando é imediatamente interrompido (`Killed` ou `Operation not permitted`) e que o evento no `tetra getevents` registra a ação tomada.

## Conexões
- [[tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel]] — Veja também: Cilium Tetragon: CRD TracingPolicy e rastreamento genérico com kprobes, tracepoints e uprobes.
- [[tetragon-monitoramento-arquivos-credenciais-execucao-privilegiada]] — Veja também: Cilium Tetragon: monitoramento de acesso a arquivos sensíveis, credenciais Linux e execução privilegiada.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
