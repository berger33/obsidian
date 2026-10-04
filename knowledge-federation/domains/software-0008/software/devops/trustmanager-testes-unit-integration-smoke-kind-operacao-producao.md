---
id: software.devops.tranche20.001920
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md", "https://cert-manager.io/docs/trust/trust-manager/", "https://github.com/cert-manager/trust-manager"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# trust-manager Qualidade e Operação: suítes `test-unit`, `test-integration`, `test-smoke` em Kind e métricas Prometheus

## Em uma frase
O projeto `trust-manager` estrutura sua validação contínua em três categorias de testes automatizados (`make test-unit`, `make test-integration` com control-plane simplificado e `make test-smoke` end-to-end em cluster **Kind** real com `cert-manager`) e expõe métricas **Prometheus** e probes de saúde no controlador.

## Por que importa
Em ambientes corporativos onde centenas de microsserviços dependem do `Bundle` para todas as conexões HTTPS/gRPC, validar upgrades do operador em um cluster efêmero Kind e monitorar falhas de reconciliação no Prometheus são práticas essenciais de SRE.

## Como funciona
Durante o desenvolvimento ou homologação de upgrades do `trust-manager`, executar `make test-smoke` provisiona um cluster Kind via Docker, instala o `cert-manager` e o `trust-manager` e valida a criação e atualização fim-a-fim dos `Bundles`.

## Exemplo
```bash
# Verificando os pods, endpoints de métricas e eventos do trust-manager no cluster:
kubectl get pods -n cert-manager -l app.kubernetes.io/name=trust-manager
kubectl get events -n cert-manager --field-selector involvedObject.kind=Bundle
```

## Limites e trade-offs
Monitore a disponibilidade do webhook do `trust-manager`, pois falhas nos certificados do webhook impediriam a criação ou edição de objetos `Bundle` na API do Kubernetes.

## Como verificar
Execute `kubectl logs -n cert-manager deploy/trust-manager --tail=50` para verificar a ausência de erros de reconciliação nos Bundles ativos.

## Conexões
- [[trustmanager-condicoes-status-synced-validacao-webhook-bundle]] — Veja também: trust-manager Status Conditions e Webhook de Validação: diagnóstico de `Synced: True` vs erros de fonte ausente.

## Fontes
- [cert-manager trust-manager GitHub — README.md (Operator for Distributing Trust Bundles Across a Kubernetes Cluster)](https://raw.githubusercontent.com/cert-manager/trust-manager/main/README.md) — README oficial do cert-manager/trust-manager descrevendo o operador e a sincronização de pacotes de confiança TLS no cluster; consultado em 2026-10-03.
- [cert-manager Official Documentation — trust-manager (Bundle CRD, Trust Namespace, Sources, Targets, JKS/PKCS12 Formats & Kubelet Caveats)](https://cert-manager.io/docs/trust/trust-manager/) — Documentação oficial do trust-manager detalhando o recurso Bundle, Trust Namespace, seletores de fontes/namespaces, JKS/PKCS12 e ressalvas de subPath; consultado em 2026-10-03.
- [cert-manager trust-manager — Official GitHub Repository](https://github.com/cert-manager/trust-manager) — Repositório oficial Apache-2.0 do cert-manager trust-manager; consultado em 2026-10-03.
