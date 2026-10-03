---
id: software.seguranca.tranche10.000990
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/cdk-team/CDK/main/README.md", "https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CDK: Perfis de Avaliação (**`--profile`**), Compilação Seletiva por **Go Build Tags (`thin`)** e Testes de Regressão de Hardening Kubernetes

## Em uma frase
Para cenários específicos de auditoria (como testar apenas configurações de Kubernetes ou rodar uma avaliação ultrarrápida em ambientes com restrição de tempo/disco), o CDK suporta selecionar perfis de avaliação via **`--profile=<nome>`** e compilar binários customizados a partir do código-fonte Go usando **Build Tags**.

## Por que importa
Ao compilar o CDK com tags seletivas, uma equipe de segurança pode gerar um binário interno de auditoria que contenha **exclusivamente o módulo `evaluate`** (removendo todos os módulos ofensivos de `exploit` para uso seguro em auditorias de conformidade de produção!).

## Como funciona
Transformar a execução de `cdk evaluate` em um job de **Verificação de Segurança de Cluster (Security Chaos / Hardening Validation)** em clusters de homologação garante que novas versões de nós, CNI ou políticas de Pod Security Standards (`restricted`) mantenham todos os vetores de escape fechados.

## Exemplo
```bash
# Executar o CDK em modo de avaliacao selecionando um perfil especifico e verificar se algum alerta 'Critical' foi emitido
cdk evaluate --profile=k8s | tee /cases/k8s-audit/cdk_eval_k8s.log
grep -E "Critical|\[!\]" /cases/k8s-audit/cdk_eval_k8s.log || echo "Nenhum vetor critico de escape detectado no container."
```

## Limites e trade-offs
Sempre execute testes com o CDK exclusivamente em clusters e containers cobertos por autorização formal de pentest e dentro de namespaces de teste dedicados.

## Como verificar
Combine os resultados de dentro do container (`cdk evaluate`) com a visão de ataque ao cluster do **Peirates (`peirates`)** para validar tanto o isolamento de nó quanto o RBAC do Kubernetes.

## Conexões
- [[cdk-entrega-binarios-containers-restritos-dev-tcp-thin-builds-deteccao]] — Veja também: Análise de Entrega *Fileless/In-Band* em Containers (`/dev/tcp`, `thin` builds) e Como **Bloquear na Camada de Runtime (`KubeArmor` / `Tracee`)**.
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Referência cruzada direta com cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate.
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.
- [[kics-auditoria-kubernetes-helm-dockerfile-pod-security-containers]] — Referência cruzada direta com kics-auditoria-kubernetes-helm-dockerfile-pod-security-containers.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
