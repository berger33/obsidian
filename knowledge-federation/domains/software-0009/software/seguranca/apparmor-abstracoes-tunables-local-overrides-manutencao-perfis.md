---
id: software.seguranca.tranche05.000485
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

# AppArmor: Modularização com `abstractions/`, Variáveis `tunables/` e Customizações Seguras em `local/`

## Em uma frase
O diretório `/etc/apparmor.d/` inclui blocos reutilizáveis de regras em **`abstractions/`** (ex.: `abstractions/base`, `abstractions/nameservice`, `abstractions/ssl_certs`, `abstractions/openssl`, `abstractions/python`), variáveis globais em **`tunables/`** (`@{HOME}`, `@{PROC}`, `@{pid}`, `@{tid}`) e o diretório de extensão **`local/`**.

## Por que importa
Escrever regras do zero para carregamento de bibliotecas C (`libc.so`), leitura de `/etc/resolv.conf` ou validação de certificados CA raiz em `/etc/ssl/certs/` tornaria os perfis frágeis; incluir `#include <abstractions/nameservice>` e `#include <abstractions/ssl_certs>` mantém os perfis enxutos e portáveis.

## Como funciona
Para customizar um perfil fornecido pela distribuição Linux (ex.: `/etc/apparmor.d/usr.sbin.mysqld`) sem sofrer conflitos de atualização de pacotes `apt`/`zypper`, os perfis oficiais terminam com `#include if exists <local/usr.sbin.mysqld>`. O administrador coloca apenas as regras extras (como um diretório de dados customizado `/mnt/nvme-db/** rwk,`) dentro de `/etc/apparmor.d/local/usr.sbin.mysqld`.

## Exemplo
```bash
# Adicionar permissao para diretorio customizado de dados no override local sem tocar no perfil principal
cat << 'EOF' | sudo tee /etc/apparmor.d/local/usr.sbin.mysqld
  # Permitir acesso ao volume NVMe dedicado de banco de dados
  /mnt/nvme-db/mysql/ r,
  /mnt/nvme-db/mysql/** rwk,
EOF

sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.mysqld
```

## Limites e trade-offs
Algumas abstrações de desktop (como `abstractions/ubuntu-browsers` ou `abstractions/user-tmp`) são amplas demais para daemons de servidor; em servidores de produção, restrinja-se a `abstractions/base`, `abstractions/nameservice` e `abstractions/ssl_certs`.

## Como verificar
Recarregue o perfil com `sudo apparmor_parser -r` e confirme que atualizações do pacote de distribuição preservam intacto o arquivo em `/etc/apparmor.d/local/`.

## Conexões
- [[apparmor-transicoes-execucao-ix-px-cx-ux-scrubbing-ambiente]] — Veja também: AppArmor: Modos de Transição de Execução (`ix`, `px`/`Px`, `cx`/`Cx`, `ux`/`Ux`) e Limpeza de Ambiente (*Environment Scrubbing*).
- [[apparmor-geracao-aprendizado-perfis-aa-genprof-aa-logprof-auditd]] — Veja também: AppArmor: Criação e Refinamento Guiado de Perfis com `aa-genprof`, `aa-logprof` e `aa-autodep`.
- [[apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal]] — Referência cruzada direta com apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal.
- [[lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh]] — Referência cruzada direta com lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
