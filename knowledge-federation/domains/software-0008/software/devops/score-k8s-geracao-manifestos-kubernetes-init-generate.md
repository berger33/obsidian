---
id: software.devops.tranche12.001114
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md", "https://raw.githubusercontent.com/score-spec/spec/main/README.md", "https://github.com/score-spec/score-k8s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Score: score-k8s para Tradução de Workloads em Manifestos Kubernetes

## Em uma frase
O `score-k8s` é a implementação de referência do Score para Kubernetes, traduzindo especificações `score.yaml` em um arquivo `manifests.yaml` contendo `Deployments`, `Services`, `Secrets`, `ConfigMaps` e recursos de dependências prontos para `kubectl apply`.

## Por que importa
Escrever manifestos Kubernetes completos do zero para cada serviço exige repetir dezenas de linhas de boilerplate de seletores, portas, volumes e injeção de segredos que poderiam ser derivadas deterministicamente de uma especificação concisa.

## Como funciona
Após inicializar o diretório de estado local (`.score-k8s/`) com `score-k8s init`, o comando `score-k8s generate score.yaml` avalia os containers, portas, probes e recursos de todos os workloads adicionados ao projeto, executa os provisionadores correspondentes e consolida a saída em `manifests.yaml`.

## Exemplo
```bash
score-k8s init --no-sample
score-k8s generate score.yaml -o manifests.yaml
kubectl apply --dry-run=client -f manifests.yaml
```

## Limites e trade-offs
Versionar o diretório `.score-k8s/` em repositórios Git compartilhados sem criptografia expõe dados sensíveis e segredos brutos persistidos no estado de geração dos provisionadores.

## Como verificar
Ignore `.score-k8s/` no Git, execute `score-k8s generate` em pipelines controlados e valide o `manifests.yaml` resultante com `kubectl apply --dry-run=server`.

## Conexões
- [[score-compose-desenvolvimento-local-docker-compose-generation]] — Veja também: Score: score-compose para Geração de Ambientes Locais Docker Compose.
- [[score-custom-provisioners-template-cmd-extensibilidade-plataforma]] — Veja também: Score: Provisionadores Customizados (template:// e cmd://) em score-compose e score-k8s.

## Fontes
- [Score Specification GitHub — README.md (score.dev/v1b1 Workload Spec, Containers, Service Ports & Resources)](https://raw.githubusercontent.com/score-spec/score-k8s/main/README.md) — README oficial da especificação Score (score-spec/spec, Apache-2.0) detalhando o contrato declarativo score.yaml v1b1, interpolação ${resources.*} e separação entre configuração agnóstica e específica de ambiente; consultado em 2026-10-03.
- [Score Reference Implementations — score-compose & score-k8s Official READMEs](https://raw.githubusercontent.com/score-spec/spec/main/README.md) — Documentação oficial das implementações de referência score-compose e score-k8s cobrindo matriz de recursos suportados, provisionadores customizados (template:// e cmd://) e --patch-templates; consultado em 2026-10-03.
- [Score — Official GitHub Organization & Repositories](https://github.com/score-spec/score-k8s) — Repositórios oficiais do projeto Score na CNCF; consultado em 2026-10-03.
