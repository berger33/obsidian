---
id: software.seguranca.tranche05.000490
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

# AppArmor: Compilação AOT, Cache Binário (`/var/cache/apparmor/`), Pré-Validação em CI e Hardening de Boot (`apparmor=1 security=apparmor`)

## Em uma frase
O compilador **`apparmor_parser`** transforma as expressões regulares e regras de texto de `/etc/apparmor.d/` em máquinas de estados determinísticas (DFA) binárias otimizadas para avaliação em tempo constante pelo kernel Linux, armazenando os binários pré-compilados em `/var/cache/apparmor/`.

## Por que importa
Compilar centenas de perfis complexos do zero a cada boot atrasaria a inicialização do servidor em vários segundos; o cache binário (`--write-cache`) permite carregar os perfis no kernel em milissegundos antes que os serviços de rede iniciem.

## Como funciona
Em pipelines de infraestrutura como código (Ansible, Packer, imagens de nós Kubernetes), `apparmor_parser -Q -K /etc/apparmor.d/<perfil>` pré-valida a sintaxe no CI (`--preprocess` / `--skip-kernel-load` `-Q`) e pré-aquece o cache binário na construção da Golden Image, enquanto os parâmetros de linha de comando do kernel no GRUB (`apparmor=1 security=apparmor` ou lista LSM `lsm=landlock,lockdown,yama,integrity,apparmor,bpf`) garantem a ativação desde o PID 1.

## Exemplo
```bash
# Pre-validar todos os perfis customizados em CI sem exigir carregamento no kernel (-Q) e atualizar cache
apparmor_parser -Q --preprocess /etc/apparmor.d/usr.local.bin.myapp > /dev/null
sudo apparmor_parser -r --write-cache /etc/apparmor.d/usr.local.bin.myapp
```

## Limites e trade-offs
Se você atualizar o kernel Linux para uma versão com novo formato de ABI de recursos LSM e o cache binário estiver corrompido ou desatualizado, limpe e reconstrua o cache com `sudo apparmor_parser -r -W -T /etc/apparmor.d/` (onde `-T` ignora a leitura do cache antigo e `-W` reescreve o novo).

## Como verificar
Verifique `cat /sys/module/apparmor/parameters/enabled` (deve retornar `Y`) e confirme a presença dos arquivos compilados em `/var/cache/apparmor/`.

## Conexões
- [[apparmor-diagnostico-violacoes-apparmor-denied-dmesg-ausearch]] — Veja também: AppArmor: Diagnóstico de Negativas (`apparmor="DENIED"`), `aa-notify` e Decodificação de Campos `operation`, `requested_mask` e `denied_mask`.
- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — Referência cruzada direta com apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles.
- [[apparmor-integracao-containers-docker-kubernetes-securitycontext]] — Referência cruzada direta com apparmor-integracao-containers-docker-kubernetes-securitycontext.
- [[lynis-hardening-sistemas-arquivos-montagens-suid-permissoes-boot]] — Referência cruzada direta com lynis-hardening-sistemas-arquivos-montagens-suid-permissoes-boot.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
