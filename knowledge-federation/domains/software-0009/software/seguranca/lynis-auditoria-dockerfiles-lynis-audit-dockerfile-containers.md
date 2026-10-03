---
id: software.seguranca.tranche05.000456
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
fontes: ["https://raw.githubusercontent.com/CISOfy/lynis/master/README.md", "https://cisofy.com/documentation/lynis/get-started/", "https://github.com/CISOfy/lynis-sdk"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CISOfy Lynis: Auditoria Estática de Imagens de Container com `lynis audit dockerfile`

## Em uma frase
Além de auditar sistemas operacionais em execução, o Lynis inclui o comando **`lynis audit dockerfile <ARQUIVO>`**, que realiza análise estática de segurança e boas práticas sobre arquivos `Dockerfile` / `Containerfile`.

## Por que importa
Permite detectar falhas de segurança na construção da imagem (como ausência da diretiva `USER` não-root, instalação de pacotes SSH/sudo desnecessários, uso da tag `:latest` ou falta de limpeza de cache de pacotes) antes mesmo do `docker build` em CI/CD.

## Como funciona
O analisador lê cada instrução (`FROM`, `RUN`, `COPY`, `ADD`, `USER`, `EXPOSE`, `ENTRYPOINT`) do `Dockerfile`, emite avisos e sugestões específicas para containers e grava os resultados estruturados em `lynis-report.dat`.

## Exemplo
```bash
# Auditar estaticamente o Dockerfile de um microsserviço usando o Lynis em modo não-interativo
lynis audit dockerfile ./deploy/Dockerfile.production --quick --no-colors
```

## Limites e trade-offs
A auditoria estática do `Dockerfile` verifica como a camada final é declarada, mas não substitui o escaneamento de CVEs nas bibliotecas instaladas dentro da imagem base (combine `lynis audit dockerfile` com Trivy/Grype).

## Como verificar
Execute `lynis audit dockerfile` contra um `Dockerfile` sem instrução `USER` e confirme que o Lynis emite o alerta recomendando execução com usuário não-privilegiado.

## Conexões
- [[lynis-hardening-openssh-ssh-7408-autenticacao-pam-limites]] — Veja também: CISOfy Lynis: Remediação de `SSH-7408` e `AUTH-*` — Hardening de OpenSSH (`sshd_config`), PAM e Contas Locais.
- [[lynis-modo-pentest-nao-privilegiado-enumeracao-escalacao-privilegio]] — Veja também: CISOfy Lynis: Execução em Modo `--pentest` (Auditoria Não-Privilegiada e Avaliação de Vetores de Escalação Local).
- [[lynis-arquitetura-auditoria-hardening-unix-linux-test-categories]] — Referência cruzada direta com lynis-arquitetura-auditoria-hardening-unix-linux-test-categories.
- [[lynis-execucao-automatizada-cronjob-systemd-timer-monitoramento-deriva]] — Referência cruzada direta com lynis-execucao-automatizada-cronjob-systemd-timer-monitoramento-deriva.
- [[apparmor-integracao-containers-docker-kubernetes-securitycontext]] — Referência cruzada direta com apparmor-integracao-containers-docker-kubernetes-securitycontext.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
