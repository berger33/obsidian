---
id: software.devops.tranche07.000625
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

# Cilium Tetragon: monitoramento de acesso a arquivos sensíveis, credenciais Linux e execução privilegiada

## Em uma frase
O Cilium Tetragon fornece casos de uso nativos baseados em eBPF para auditar e restringir o acesso a arquivos sensíveis (FIM), alterações de credenciais/capabilities de processos Linux e execuções privilegiadas.

## Por que importa
Ataques pós-exploração em containers frequentemente envolvem a leitura de tokens de ServiceAccount do Kubernetes (`/var/run/secrets/kubernetes.io/serviceaccount/token`), modificação de binários do sistema ou escalada de privilégios no kernel (alterando o `uid` para `0` ou adquirindo `CAP_SYS_ADMIN`). Segundo o README e a visão geral oficial do Tetragon, enganchar diretamente nas funções de verificação de segurança do kernel (LSM / VFS / credenciais) evita as falhas clássicas do rastreamento de syscalls, onde ponteiros em espaço de usuário podem ser alterados maliciosamente por atacantes ou falhar por page faults.

## Como funciona
Para monitoramento de acesso a arquivos (`filename access`), o Tetragon engancha em funções internas do Virtual File System (VFS) e Linux Security Modules (como `security_file_permission`, `security_mmap_file` e `security_path_truncate`), onde a estrutura `struct file` do kernel já foi resolvida de forma imutável, permitindo filtrar por caminhos exatos ou prefixos de diretórios. Para monitoramento de credenciais e execução privilegiada (`linux-process-credentials` e `privileged-execution`), o Tetragon inspeciona as estruturas `struct cred` e namespaces do kernel em `commit_creds` ou durante a transição de processos, detectando imediatamente quando uma tarefa adquire novas capabilities Linux, muda de namespace (container escape) ou altera seu UID/GID efetivo.

## Exemplo
```bash
# Observar eventos de leitura/escrita em arquivos sensíveis monitorados em JSON via CLI tetra
tetra getevents -o json --namespace producao --event-types PROCESS_KPROBE | jq .process_kprobe
```

## Limites e trade-offs
Monitorar leituras em diretórios inteiros de alto tráfego (como `/usr/lib` ou `/var/log`) sem filtrar por binários ou operações de escrita pode gerar milhares de eventos por segundo; para File Integrity Monitoring (FIM) eficiente em produção, deve-se restringir `matchArgs` a caminhos críticos (como `/etc/`, `/root/.ssh/`, tokens de segredos) ou filtrar apenas máscaras de escrita (`MAY_WRITE` / `MAY_APPEND`).

## Como verificar
Aplique uma política de monitoramento de arquivos sensíveis ou credenciais e execute um teste controlado de leitura do arquivo monitorado, confirmando que o evento gerado inclui o caminho completo do arquivo, o binário executor, o pod e as capabilities do processo.

## Conexões
- [[tetragon-enforcement-kernel-sigkill-override-bloqueio-tempo-real]] — Veja também: Cilium Tetragon: runtime enforcement síncrono no kernel com ações Sigkill e Override.
- [[tetragon-observabilidade-rede-sockets-processos-ebpf]] — Veja também: Cilium Tetragon: observabilidade de rede correlacionando sockets TCP/UDP diretamente a processos e pods.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.
- [[tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel]] — Referência cruzada direta com tetragon-tracingpolicy-kprobes-tracepoints-uprobes-kernel.

## Fontes
- [Cilium Tetragon GitHub — README.md (Process Lifecycle, TracingPolicy & Tetra CLI)](https://raw.githubusercontent.com/cilium/tetragon/main/README.md) — README oficial do Cilium Tetragon cobrindo eventos process_exec/process_exit, rastreamento genérico com kprobes/tracepoints/uprobes via TracingPolicy e casos de uso em Kubernetes e Linux; consultado em 2026-10-03.
- [Cilium Tetragon Official Documentation — Overview & eBPF Real-Time Enforcement](https://tetragon.io/docs/overview/) — Visão geral técnica do Cilium Tetragon detalhando filtragem e bloqueio síncrono em eBPF dentro do kernel Linux e enriquecimento com identidades do Kubernetes; consultado em 2026-10-03.
- [Cilium Tetragon — Official GitHub Repository](https://github.com/cilium/tetragon) — Repositório oficial do Cilium Tetragon na CNCF; consultado em 2026-10-03.
