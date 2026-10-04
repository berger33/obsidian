# MOC — Operação e segurança Kubernetes

Notas autorais do lote `software-kubernetes-operacao-0005`. Este mapa organiza navegação e não substitui revisão factual nem testes no cluster.

## Disponibilidade e capacidade
- [[probes-kubernetes-liveness-readiness-startup]] — inicialização, prontidão e reinicialização.
- [[requests-limits-cpu-memoria-kubernetes]] — scheduling e limites de CPU/memória.
- [[deployment-rolling-update-kubernetes]] — troca gradual de réplicas.
- [[hpa-autoscaling-kubernetes]] — ajuste horizontal por métricas.
- [[pdb-disponibilidade-kubernetes]] — orçamento de interrupções voluntárias.

## Segurança do plano de dados e API
- [[secrets-kubernetes-protecao-dados]] — proteção de credenciais e dados sensíveis.
- [[rbac-kubernetes-serviceaccounts]] — identidade de workloads e autorização da API.
- [[networkpolicy-kubernetes-isolamento]] — restrições de conexões de rede.

## Revisão
As 8 notas do lote 0005 tiveram revisão factual humana confirmada pelo usuário em 2026-10-02 e contam como válidas; o passe automático, isoladamente, não substitui essa revisão.
