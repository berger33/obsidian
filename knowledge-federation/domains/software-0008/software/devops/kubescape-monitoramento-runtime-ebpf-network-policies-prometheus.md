---
id: software.devops.tranche07.000646
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
fontes: ["https://raw.githubusercontent.com/kubescape/kubescape/master/README.md", "https://kubescape.io/docs/operator/", "https://github.com/kubescape/kubescape"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubescape: detecção de ameaças em runtime com eBPF (Inspektor Gadget) e geração de NetworkPolicies

## Em uma frase
No modo Operator, o Kubescape utiliza monitoramento em tempo de execução baseado em eBPF via Inspektor Gadget para detectar ameaças em containers, gerar perfis de aplicação, sintetizar `NetworkPolicies` e exportar métricas Prometheus.

## Por que importa
Criar `NetworkPolicies` do Kubernetes manualmente para dezenas de microsserviços é propenso a erros que bloqueiam tráfego legítimo, e confiar apenas em varreduras estáticas de imagens não detecta ataques zero-day ou execuções anômalas em memória. De acordo com o README oficial do Kubescape, o operador combina telemetria eBPF em tempo real (construída sobre o Inspektor Gadget) para observar o comportamento real de cada workload e transformá-lo em políticas de rede e alertas de runtime.

## Como funciona
O agente de nó do Kubescape (executado como DaemonSet pelo `kubescape-operator`) utiliza o framework eBPF do **Inspektor Gadget** para observar chamadas de sistema, processos executados, arquivos abertos, capabilities utilizadas e conexões de rede de entrada e saída de cada pod durante um período de aprendizado. Com base nesse perfil comportamental observado no kernel, o Kubescape: (1) gera recomendações precisas de `NetworkPolicy` de menor privilégio refletindo apenas as comunicações reais do serviço; (2) identifica quais pacotes e arquivos da imagem são efetivamente carregados em memória (relevância de vulnerabilidades em runtime); e (3) dispara alertas de detecção de ameaças quando um container executa um processo, abre um arquivo ou estabelece uma conexão fora do seu perfil aprendido, além de expor a postura de segurança como métricas Prometheus.

## Exemplo
```bash
# Verificar os pods do operador Kubescape (incluindo o agente de nó eBPF) e inspecionar objetos gerados
kubectl get pods -n kubescape
kubectl get networkneighborhoods,applicationprofiles -A
```

## Limites e trade-offs
Para que a geração automática de `NetworkPolicies` e a detecção de anomalias baseada em perfis (`ApplicationProfile`) não gerem falsos positivos em produção, o período de aprendizado inicial precisa cobrir todos os fluxos legítimos do serviço (incluindo rotinas periódicas, jobs de backup e caminhos de erro raros); encerrar o aprendizado prematuramente fará com que tarefas agendadas legítimas sejam sinalizadas como comportamento anômalo.

## Como verificar
No cluster com o `kubescape-operator` ativo, verifique a criação dos recursos de perfil comportamental e de vizinhança de rede para os pods em execução e valide a exposição de métricas no endpoint Prometheus do operador.

## Conexões
- [[kubescape-operador-in-cluster-monitoramento-continuo-helm]] — Veja também: Kubescape Operator: monitoramento contínuo in-cluster de configuração, CVEs e runtime via Helm.
- [[kubescape-execucao-offline-air-gapped-protecao-metadados]] — Veja também: Kubescape: operação offline/air-gapped (kubescape download) e proteção de metadados com pseudonimização e criptografia.
- [[inspektor-integracao-biblioteca-golang-kubescape-ecossistema]] — Referência cruzada direta com inspektor-integracao-biblioteca-golang-kubescape-ecossistema.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
