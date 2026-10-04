---
id: software.seguranca.tranche03.000213
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

# KubeArmor Controle Fino de Execução de Processos: `fromSource`, `ownerOnly` e `matchDirectories` recursivos

## Em uma frase
Na seção **`process`** de uma `KubeArmorPolicy`, cada regra em `matchPaths` ou `matchDirectories` suporta três modificadores poderosos documentados na especificação oficial: **`fromSource`** (restringe qual binário pai pode ou não invocar o executável alvo), **`ownerOnly: true`** (permite a execução apenas pelo usuário proprietário do arquivo binário) e **`recursive: true`** (estende a regra a todos os subdiretórios).

## Por que importa
Bloquear `/bin/sh` ou `/usr/bin/env` globalmente em todo o container pode quebrar o script de entrypoint legítimo da aplicação na inicialização; porém, o processo do servidor web (ex.: `/usr/sbin/nginx` ou `/usr/local/bin/node`) nunca deveria invocar `/bin/sh` ou `/bin/bash` depois de iniciado!

## Como funciona
Especificando **`fromSource: [{path: /usr/sbin/nginx}]`** com `action: Block` sobre `/bin/bash` e `/bin/sh`, scripts de inicialização continuam funcionando normalmente, mas qualquer tentativa de *Command Injection / Web Shell* originada do processo `nginx` recebe erro imediato `Permission denied (EACCES)` do kernel!

## Exemplo
```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: ksp-nginx-block-shell-spawn
  namespace: production
spec:
  severity: 9
  selector:
    matchLabels:
      app: frontend-nginx
  process:
    matchPaths:
      - path: /bin/sh
        fromSource:
          - path: /usr/sbin/nginx
      - path: /bin/bash
        fromSource:
          - path: /usr/sbin/nginx
  action: Block
```

## Limites e trade-offs
Conforme a documentação oficial, evite usar `matchPatterns` (expressões regulares) em regras `process` a menos que necessário, pois a cobertura de regex depende das particularidades do perfil AppArmor; prefira sempre `matchPaths` e `matchDirectories` explícitos.

## Como verificar
Teste executar `kubectl exec -it <pod> -- /bin/sh` versus spawna-lo a partir do binário restrito em `fromSource` e observe o alerta em `karmor logs`.

## Conexões
- [[kubearmor-crd-kubearmorpolicy-especificacao-selector-process-file-network]] — Veja também: KubeArmor `KubeArmorPolicy` (`ksp`): anatomia da política para Pods/Containers (`selector`, `process`, `file`, `network`, `capabilities`, `action`).
- [[kubearmor-protecao-arquivos-sensi-readonly-fromsource-serviceaccount-token]] — Veja também: KubeArmor Proteção de Arquivos e Segredos (`file`): `readOnly: true`, vínculo `fromSource` e blindagem do Token da ServiceAccount.

## Fontes
- [CNCF KubeArmor GitHub — README.md (Cloud-Native Runtime Security Enforcement System, LSMs AppArmor/SELinux/BPF-LSM, eBPF & Architecture)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/getting-started/security_policy_specification.md) — README oficial do kubearmor/KubeArmor descrevendo o bloqueio inline no kernel via LSMs, casos de uso Zero-Trust e ecossistema karmor; consultado em 2026-10-03.
- [CNCF KubeArmor Official Documentation — Security Policy Specification for Containers (KubeArmorPolicy selector, process, file, network, capabilities & action)](https://raw.githubusercontent.com/kubearmor/KubeArmor/main/README.md) — Especificação oficial da KubeArmorPolicy detalhando matchPaths, matchDirectories, fromSource, ownerOnly, readOnly e ações Allow/Audit/Block; consultado em 2026-10-03.
- [CNCF KubeArmor — Official GitHub Repository](https://github.com/kubearmor/KubeArmor) — Repositório oficial Apache-2.0 do CNCF KubeArmor; consultado em 2026-10-03.
