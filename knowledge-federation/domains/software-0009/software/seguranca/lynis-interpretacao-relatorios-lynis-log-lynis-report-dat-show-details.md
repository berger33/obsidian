---
id: software.seguranca.tranche05.000452
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

# CISOfy Lynis: Análise de `Warnings` vs `Suggestions`, `/var/log/lynis-report.dat` e `lynis show details <TEST-ID>`

## Em uma frase
Cada achado do Lynis recebe um identificador alfanumérico único de teste (ex.: `SSH-7408`, `KRNL-6000`, `AUTH-9286`, `FILE-6310`) e é classificado como **Warning** (problema crítico ou falha de controle ativo) ou **Suggestion** (recomendação de endurecimento adicional).

## Por que importa
A saída de tela mostra apenas o resumo; para entender exatamente qual linha de arquivo de configuração ou parâmetro `sysctl` motivou um `Warning` ou `Suggestion`, o engenheiro utiliza `lynis show details <TEST-ID>`.

## Como funciona
O comando `sudo lynis show details SSH-7408` extrai de `/var/log/lynis.log` todas as verificações internas daquele ID (por exemplo, `PermitRootLogin`, `X11Forwarding`, `MaxAuthTries`, `AllowTcpForwarding`, `ClientAliveCountMax`), indicando quais valores estavam em conformidade (`OK`) e quais precisam ser ajustados (`DIFFERENT` / `WARNING`). Já `/var/log/lynis-report.dat` armazena pares `chave=valor` prontos para parsing automatizado.

## Exemplo
```bash
# Extrair todos os warnings e suggestions do relatório estruturado e inspecionar o detalhe do teste SSH-7408
sudo grep -E "^(warning|suggestion)\[\]=" /var/log/lynis-report.dat
sudo lynis show details SSH-7408
```

## Limites e trade-offs
O arquivo `/var/log/lynis.log` é sobrescrito a cada nova execução do Lynis; se precisar preservar o histórico de auditoria para comparação forense ou conformidade, arquive `/var/log/lynis.log` e `/var/log/lynis-report.dat` com carimbo de data após cada scan.

## Como verificar
Execute `sudo lynis show details KRNL-6000` após uma auditoria e confirme a listagem individual de cada chave `sysctl` avaliada pelo teste.

## Conexões
- [[lynis-arquitetura-auditoria-hardening-unix-linux-test-categories]] — Veja também: CISOfy Lynis: Arquitetura de Auditoria Local e Hardening de Sistemas Linux/Unix (`lynis audit system`).
- [[lynis-perfis-customizados-custom-prf-skip-test-sysctl-ssh]] — Veja também: CISOfy Lynis: Customização de Políticas com Perfis `custom.prf` (`skip-test`, `config-data` e `--profile`).
- [[lynis-hardening-kernel-sysctl-krnl-6000-aslr-ptrace-bpf-rede]] — Referência cruzada direta com lynis-hardening-kernel-sysctl-krnl-6000-aslr-ptrace-bpf-rede.
- [[lynis-hardening-openssh-ssh-7408-autenticacao-pam-limites]] — Referência cruzada direta com lynis-hardening-openssh-ssh-7408-autenticacao-pam-limites.

## Fontes
- [CISOfy Lynis Official GitHub — Security Auditing and Hardening Tool](https://raw.githubusercontent.com/CISOfy/lynis/master/README.md) — documentação oficial do CISOfy Lynis para auditoria de segurança, conformidade e hardening Unix/Linux; consultado em 2026-10-03.
- [CISOfy Official Documentation — Lynis Get Started & Commands](https://cisofy.com/documentation/lynis/get-started/) — guia oficial de comandos, opções (--quick, --cronjob, --pentest), logs e relatórios do Lynis; consultado em 2026-10-03.
- [CISOfy Lynis SDK — Custom Tests Development](https://github.com/CISOfy/lynis-sdk) — kit oficial de desenvolvimento de testes customizados para o Lynis; consultado em 2026-10-03.
