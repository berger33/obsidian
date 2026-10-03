---
id: software.seguranca.tranche03.000224
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md", "https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md", "https://github.com/aquasecurity/tracee"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Tracee Filtros de Eventos (`rules[].filters`): operadores sobre `data.*`, `retval`, `uid`, `comm` e wildcards `*` de prefixo/sufixo

## Em uma frase
Dentro de cada regra da seção **`rules`** de uma política do Tracee, a lista **`filters`** permite filtrar tanto pelos **argumentos específicos do evento (`data.<arg_name>`)** quanto pelo **valor de retorno (`retval`)** e pelos **campos de contexto da tarefa** (`uid`, `pid`, `mntns`, `comm`, `cgroupId`, `container.image`, `k8s.namespace`), suportando igualdade (`=`), diferença (`!=`), comparações numéricas (`<`, `>`) e wildcards de prefixo/sufixo (`*`)!

## Por que importa
Rastrear todo evento `security_file_open` sem filtro captura milhares de leituras normais por segundo; mas filtrar especificamente por aberturas de `/etc/shadow` ou `/root/.ssh/*` que **tiveram sucesso (`retval=0`)** por processos cujo nome não seja `sshd` entrega um alerta cirúrgico de alta fidelidade.

## Como funciona
Quando múltiplos valores são separados por vírgula no mesmo filtro (ex.: `data.pathname=/etc/shadow,/etc/sudoers`), eles operam como um **`OR`** lógico; já múltiplos itens separados na lista `filters` operam como um **`AND`** lógico!

## Exemplo
```yaml
type: policy
name: detect-credential-file-access
description: Alerta quando um processo em container abre arquivos sensíveis de credenciais
scope:
  - container
rules:
  - event: security_file_open
    filters:
      - data.pathname=/etc/shadow,/etc/gshadow,/root/.ssh/*,*/.aws/credentials
      - comm!=sshd,login,passwd
```

## Limites e trade-offs
Para consultar todos os nomes exatos de argumentos (`data.*`) aceitos por um evento específico antes de escrever o filtro, execute **`tracee list <nome_do_evento>`** na CLI.

## Como verificar
Valide o filtro executando `cat /etc/shadow` em um container de teste e observando o JSON emitido pelo Tracee.

## Conexões
- [[tracee-policy-scopes-container-not-container-tree-pid-executable]] — Veja também: Tracee Escopos de Política (`scope`): filtragem no kernel por `container`, `host`, árvore de processos (`tree`), `executable` e `uid`.
- [[tracee-built-in-security-events-signatures-fileless-rootkit-escape]] — Veja também: Tracee Assinaturas de Segurança Embutidas: detecção de execução *Fileless* (`mem_prot_alert`), *Rootkits* (` hooked_syscall`), `anti_debugging` e Escape.

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
