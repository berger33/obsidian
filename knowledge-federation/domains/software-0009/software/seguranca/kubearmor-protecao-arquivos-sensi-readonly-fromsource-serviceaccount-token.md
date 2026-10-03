---
id: software.seguranca.tranche03.000214
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
fontes: ["https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md", "https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md", "https://github.com/kubearmor/KubeArmor"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# KubeArmor Proteção de Arquivos e Segredos (`file`): `readOnly: true`, vínculo `fromSource` e blindagem do Token da ServiceAccount

## Em uma frase
A seção **`file`** da `KubeArmorPolicy` permite controlar leituras e escritas em arquivos (`matchPaths`) e diretórios (`matchDirectories`) dentro do container, suportando as opções **`readOnly: true`** (permite leitura, mas bloqueia qualquer modificação, exclusão ou escrita), **`ownerOnly: true`** e **`fromSource`** (restringe qual binário específico tem permissão de acessar aquele arquivo!).

## Por que importa
Mesmo que um container precise montar um certificado privado TLS (`/etc/ssl/private/tls.key`) ou o token da ServiceAccount do Kubernetes (`/run/secrets/kubernetes.io/serviceaccount/token`), **apenas o binário principal da aplicação** precisa ler esse arquivo — nunca um `curl`, `cat` ou `python` executado por um invasor!

## Como funciona
Combinando `action: Allow` (ou `Block` seletivo) com `fromSource`, ou aplicando `readOnly: true` sobre diretórios de binários (`/bin/`, `/usr/bin/`, `/lib/`) e pastas de configuração, o KubeArmor transforma sistemas de arquivos mutáveis em perfis imutáveis no kernel.

## Exemplo
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-protect-sa-token-and-etc
  namespace: production
spec:
  severity: 10
  message: "Acesso ao token da ServiceAccount ou escrita em /etc bloqueados"
  selector:
    matchLabels:
      app: payment-worker
  file:
    matchPaths:
      - path: /var/run/secrets/kubernetes.io/serviceaccount/token
    matchDirectories:
      - dir: /etc/
        recursive: true
        readOnly: true
  action: Block
```

## Limites e trade-offs
Lembre-se de que em Pods Kubernetes modernos o token da ServiceAccount é montado em `/var/run/secrets/kubernetes.io/serviceaccount/` (que frequentemente é um symlink para `/run/secrets/kubernetes.io/serviceaccount/`); proteja o caminho real resolvido no filesystem do container.

## Como verificar
Teste tentar ler o token ou criar um arquivo em `/etc/test` dentro do Pod e verifique o bloqueio `Permission denied`.

## Conexões
- [[kubearmor-restricao-processos-fromsource-owneronly-recursive]] — Veja também: KubeArmor Controle Fino de Execução de Processos: `fromSource`, `ownerOnly` e `matchDirectories` recursivos.
- [[kubearmor-restricao-rede-capabilities-socket-icmp-tcp-udp-por-processo]] — Veja também: KubeArmor Controle de Rede (`network`) e Linux Capabilities (`capabilities`) por Executável (`fromSource`).

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
