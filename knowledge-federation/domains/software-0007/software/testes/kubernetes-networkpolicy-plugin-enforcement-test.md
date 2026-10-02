---
id: software.testes.tranche09.000303
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://kubernetes.io/docs/concepts/services-networking/network-policies/", "https://kubernetes.io/docs/concepts/workloads/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kubernetes NetworkPolicy: testar enforcement do plugin de rede

## Em uma frase
Uma NetworkPolicy só tem efeito se a solução de rede do cluster implementar enforcement da API.

## Por que importa
Controladores Kubernetes reconciliam estado de forma assíncrona, então uma assertion instantânea sobre Pod isolado não representa necessariamente o resultado desejado. Aplicar YAML e vê-lo aceito pelo API server não prova que tráfego foi bloqueado ou permitido.

## Como funciona
Teste objetos e condições observáveis em cluster isolado, aguarde convergência com timeout e valide identidades e plugins que participam do comportamento. Teste conexões desde Pods selecionados e não selecionados para destinos e portas incluídos e excluídos na regra.

## Exemplo
Policy de banco permite ingress do frontend; pod de namespace diferente tenta a mesma porta e deve falhar no ambiente compatível.

## Limites e trade-offs
Comportamento depende da versão, controller, scheduler e plugins instalados; dry-run do API server não prova execução de rede ou workload. Políticas são aditivas e resultados dependem do conjunto de policies e do plugin; não conclua isolamento por objeto criado.

## Como verificar
Identifique o CNI instalado, teste ingress e egress a partir de Pods reais e verifique também tráfego de resposta.

## Conexões
- [[kubernetes-deployment-rollout-observed-state]] — Veja também: Kubernetes Deployment: aguardar rollout e validar aplicação.
- [[kubernetes-rbac-auth-can-i-identity]] — Veja também: Kubernetes RBAC: verificar permissão com identidade e escopo.

## Fontes
- [Kubernetes — Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) — políticas ingress/egress e requisito de plugin que as implemente; consultado em 2026-10-02.
- [Kubernetes — Workloads](https://kubernetes.io/docs/concepts/workloads/) — controladores e reconciliação de workloads; consultado em 2026-10-02.
