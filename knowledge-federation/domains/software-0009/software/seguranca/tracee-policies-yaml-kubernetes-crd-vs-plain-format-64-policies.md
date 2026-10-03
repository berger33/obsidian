---
id: software.seguranca.tranche03.000222
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

# Tracee Políticas de Detecção (`Policies`): intercambiabilidade entre formato `Kubernetes CRD` (`tracee.aquasec.com/v1beta1`) e `Plain YAML`

## Em uma frase
Conforme documentado na referência oficial *Policies* (`docs/docs/policies/index.md`), o Tracee permite carregar simultaneamente **até 64 políticas independentes** que definem quais eventos (`rules`) devem ser rastreados em quais cargas de trabalho (`scope`), suportando dois formatos 100% intercambiáveis: o **formato Kubernetes CRD (`apiVersion: tracee.aquasec.com/v1beta1`, `kind: Policy`)** e o **formato Plain YAML (`type: policy`)**.

## Por que importa
Ter uma sintaxe diferente para testar regras localmente na CLI do laptop e outra sintaxe para implantar no cluster Kubernetes via GitOps (Argo CD / Flux) gera erros de tradução.

## Como funciona
O Tracee **detecta automaticamente o formato** de cada arquivo verificando a presença de `type: policy` ou `apiVersion`/`kind`, permitindo inclusive misturar arquivos de ambos os formatos no mesmo diretório passado para `--policy`!

## Exemplo
```yaml
apiVersion: tracee.aquasec.com/v1beta1
kind: Policy
metadata:
  name: detect-suspicious-tmp-execution
  annotations:
    description: Detecta binários soltos em memória/disco e abertura de arquivos em /tmp
spec:
  scope:
    - container=new
  rules:
    - event: dropped_executable
    - event: security_file_open
      filters:
        - data.pathname=/tmp/*
```

## Limites e trade-offs
Atenção à regra de validação documentada em `docs/docs/policies/index.md`: **cada tipo de evento (`event`) só pode ser declarado uma única vez dentro de uma mesma política**, e toda política deve conter obrigatoriamente os campos `name`, `description`, `scope` e `rules`.

## Como verificar
Carregue e valide seu diretório de políticas executando `tracee --policy ./minhas-politicas/`.

## Conexões
- [[tracee-arquitetura-aqua-security-ebpf-runtime-security-forensics]] — Veja também: Aqua Security Tracee: arquitetura unificada *"Everything is an Event"* para segurança em runtime e forense com `eBPF`.
- [[tracee-policy-scopes-container-not-container-tree-pid-executable]] — Veja também: Tracee Escopos de Política (`scope`): filtragem no kernel por `container`, `host`, árvore de processos (`tree`), `executable` e `uid`.

## Fontes
- [Aqua Security Tracee Official Documentation — Overview (Everything is an Event Architecture, 400+ Syscalls, Built-in Signatures, Forensic Capture & Security Model)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/policies/index.md) — Visão geral oficial da documentação do Tracee detalhando o pipeline unificado de eventos, assinaturas de detecção embutidas, coleta forense e modelo de ameaças; consultado em 2026-10-03.
- [Aqua Security Tracee Official Documentation — Policies Reference (Kubernetes CRD v1beta1 vs Plain Format, 64 Policies, Scopes & Event Filters)](https://raw.githubusercontent.com/aquasecurity/tracee/main/docs/docs/overview.md) — Referência oficial de políticas do Tracee explicando a intercambiabilidade entre o formato CRD Kubernetes e Plain YAML, escopos e filtros; consultado em 2026-10-03.
- [Aqua Security Tracee — Official GitHub Repository](https://github.com/aquasecurity/tracee) — Repositório oficial Apache-2.0 do Aqua Security Tracee; consultado em 2026-10-03.
