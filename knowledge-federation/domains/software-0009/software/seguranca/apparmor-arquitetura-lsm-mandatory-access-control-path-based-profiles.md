---
id: software.seguranca.tranche05.000481
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://gitlab.com/apparmor/apparmor/-/raw/master/README.md", "https://gitlab.com/apparmor/apparmor/-/wikis/home", "https://gitlab.com/apparmor/apparmor/-/wikis/Documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# AppArmor: Arquitetura do Módulo LSM de Controle de Acesso Obrigatório (MAC Baseado em Caminhos e Confinamento de Superusuário)

## Em uma frase
**AppArmor** (`gitlab.com/apparmor/apparmor`, GPLv2 / LGPL para `libapparmor`) é um sistema de *Mandatory Access Control* (MAC) integrado ao framework Linux Security Module (LSM) desde o kernel 2.6.36 (e padrão no Ubuntu, Debian, SUSE e derivados) que confina processos individuais por meio de perfis declarativos baseados em caminhos de arquivos.

## Por que importa
Diferente do controle de acesso discricionário tradicional (DAC — permissões `rwx` e proprietário), as restrições do AppArmor são obrigatórias e aplicam-se inclusive a processos executando como **`root` (UID 0)**: se um daemon web vulnerável rodando como root for explorado, o perfil AppArmor impede que ele leia `/etc/shadow`, carregue módulos de kernel ou execute `/bin/sh` se não estiverem explicitamente listados no perfil.

## Como funciona
Os perfis de texto residem em `/etc/apparmor.d/`, são compilados para bytecode binário pelo `apparmor_parser` (com cache em `/var/cache/apparmor/`) e carregados no kernel. Processos sem perfil aplicável rodam `unconfined`, permitindo adoção incremental focada nos daemons expostos à rede.

## Exemplo
```bash
# Verificar o status do modulo AppArmor no kernel e a contagem de perfis em modo enforce e complain
sudo aa-status
```

## Limites e trade-offs
Como o AppArmor resolve políticas de arquivo pelo caminho (*pathname*), a criação de *hard links* para um arquivo sensível em um diretório não protegido permitiria contornar uma regra baseada apenas no caminho original se o perfil também não restringir operações `link` ou se `fs.protected_hardlinks = 1` não estiver ativo no kernel.

## Como verificar
Execute `sudo aa-enabled && sudo aa-status --json | jq '.profiles | length'` para confirmar que o LSM está ativo e carregando perfis.

## Conexões
- [[apparmor-modos-operacao-enforce-complain-audit-deny-aa-enforce]] — Veja também: AppArmor: Modos de Operação de Perfis (`enforce`, `complain`, `unconfined`, `kill`) e Comandos `aa-enforce`, `aa-complain` e `aa-disable`.
- [[apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal]] — Referência cruzada direta com apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal.
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Referência cruzada direta com selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
