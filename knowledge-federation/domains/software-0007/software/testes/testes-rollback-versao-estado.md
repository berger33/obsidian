---
id: software.testes.tranche07.000138
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/", "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de rollback e compatibilidade de estado", "Teste: Teste de rollback e compatibilidade de estado"]
lote: software-testes-2000-0001
---

# Teste de rollback e compatibilidade de estado

## Em uma frase
Prove que uma implantação problemática pode ser revertida e que a versão anterior opera com o estado produzido durante a atualização.

## Por que importa
Rollback da imagem pode não desfazer migração de banco, mensagens ou alterações irreversíveis; a recuperação precisa cobrir o contrato entre versões.

## Como funciona
Em ambiente de teste, promova uma versão defeituosa controlada, detecte falha por critério observável, execute rollback e verifique tráfego, schema e jobs em andamento. Teste estratégia expand-contract para alterações de dados.

## Exemplo
Aplique uma imagem que falha no readiness, confirme rollout interrompido e reverta para revisão anterior; depois valide consulta e escrita sobre o schema atual sem perda de dados de teste.

## Limites e trade-offs
Rollback de Deployment não reverte automaticamente efeitos externos ou migrações. Não teste com release destrutiva em produção; compatibilidade depende de procedimento específico do sistema.

## Como verificar
Confirme revisão implantada após undo, readiness, smoke tests e invariantes de dados; registre tempo de detecção e retorno e valide se a versão antiga pode ler/escrever o schema expandido.

## Conexões
- [[deployment-rolling-update-kubernetes]] — aprofundamento relacionado.
- [[migracoes-expand-contract]] — aprofundamento relacionado.

## Fontes
- [Kubernetes — Performing a Rolling Update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) — verificação de update e exercício de rollback; consultado em 2026-10-01.
- [Kubernetes — Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) — rollouts progressivos, status, revisão e rollback de Deployment; consultado em 2026-10-01.
